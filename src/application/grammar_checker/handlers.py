from src.application.interfaces.text_gears import ITextGears
from src.application.interfaces.trinka_grammar_checker import ITrinkaGrammarChecker
from src.domain.analysis.entities import (
    UnifiedError,
    UnifiedErrorComparison,
    UnifiedErrorProvider,
)
from src.domain.text_gears.entities import (
    TextGearsTextToCheck,
    TextGearsGrammarCheckerObject,
)
from src.domain.trinka_grammar_checker.entities import (
    TrinkaTextToCheck,
    TrinkaCheckResult,
)


class GrammarCheckerHandler:
    """
    Обработчик проверки грамматики.

    Класс инкапсулирует работу сразу с двумя провайдерами:
    - TextGears
    - Trinka Grammar Checker

    Через данный обработчик можно:
    - запускать проверку грамматики текста отдельно через TextGears
    - запускать проверку грамматики текста отдельно через Trinka
    - выполнять унифицированный анализ и сравнение результатов двух сервисов
    """

    def __init__(
        self, text_gears: ITextGears, trinka_grammar_checker: ITrinkaGrammarChecker
    ):
        self.text_gears = text_gears
        self.trinka_grammar_checker = trinka_grammar_checker

    async def grammar_check_text_gears(
        self, text: str, language: str
    ) -> TextGearsGrammarCheckerObject:
        """
        Проверка текста с помощью TextGears API

        Args:
            text (str): исходный текст для проверки
            language (str): язык текста (в формате ISO, например "en-US")

        Returns:
            TextGearsGrammarCheckerObject: результат проверки от TextGears

        Raises:
            ValueError: если входные данные некорректны (валидация внутри value-object).
            InfrastructureError: если произошла ошибка при обращении к API.
            RapidApiError: если API вернул ошибку.
        """
        text_to_check = TextGearsTextToCheck(text=text, language=language)

        grammar_checked_object: TextGearsGrammarCheckerObject = (
            await self.text_gears.grammar_check(text_to_check)
        )

        return grammar_checked_object

    async def grammar_check_trinka(self, text: str, language: str) -> TrinkaCheckResult:
        """
        Проверка текста с помощью Trinka Grammar Checker API

        Args:
            text (str): исходный текст для проверки
            language (str): язык текста (короткий код ISO, например "en")

        Returns:
            TrinkaCheckResult: результат проверки от Trinka

        Raises:
            ValueError: если входные данные некорректны (валидация внутри value-object)
            InfrastructureError: если произошла ошибка при обращении к API
            RapidApiError: если API вернул ошибку
        """
        text_to_check = TrinkaTextToCheck(paragraph=text, language=language)

        grammar_checked_object: TrinkaCheckResult = (
            await self.trinka_grammar_checker.grammar_check(text_to_check)
        )

        return grammar_checked_object

    def unified_analyze(
        self,
        tg_result: TextGearsGrammarCheckerObject,
        trinka_result: TrinkaCheckResult,
    ) -> UnifiedErrorComparison:
        """
        Унифицированный анализ результатов двух сервисов (TextGears и Trinka)

        Сравнивает списки ошибок, найденные разными провайдерами, и выделяет
        - ошибки, найденные обоими сервисами (common)
        - ошибки, уникальные для TextGears (only_text_gears)
        - ошибки, уникальные для Trinka (only_trinka)

        Args:
            tg_result (TextGearsGrammarCheckerObject): результат проверки от TextGears
            trinka_result (TrinkaCheckResult): результат проверки от Trinka

        Returns:
            UnifiedErrorComparison: результат сравнения ошибок
        """
        print(tg_result)
        print(trinka_result)
        tg_errors: list[UnifiedError] = []
        for e in tg_result.response.errors:
            tg_errors.append(
                UnifiedError(
                    offset=e.offset,
                    length=e.length,
                    covered_text=e.bad,
                    suggestions=e.better,
                    comment=next(iter(e.description.values()), None),
                    category=e.type.value,
                    provider=UnifiedErrorProvider.TEXT_GEARS,
                )
            )

        trinka_errors: list[UnifiedError] = []
        for sent in trinka_result.sentences:
            for r in sent.result:
                trinka_errors.append(
                    UnifiedError(
                        offset=sent.begin + r.start_index,
                        length=r.end_index - r.start_index,
                        covered_text=r.covered_text,
                        suggestions=r.output,
                        comment=r.comment[0] if r.comment else None,
                        category=r.error_category[0] if r.error_category else "unknown",
                        provider=UnifiedErrorProvider.TRINKA,
                    )
                )

        def key(err: UnifiedError) -> tuple[int, int, str]:
            return err.offset, err.length, err.covered_text.lower()

        tg_keys = {key(e): e for e in tg_errors}
        trinka_keys = {key(e): e for e in trinka_errors}

        common = [err for k, err in tg_keys.items() if k in trinka_keys]
        only_tg = [err for k, err in tg_keys.items() if k not in trinka_keys]
        only_trinka = [err for k, err in trinka_keys.items() if k not in tg_keys]

        return UnifiedErrorComparison(
            common=common, only_text_gears=only_tg, only_trinka=only_trinka
        )
