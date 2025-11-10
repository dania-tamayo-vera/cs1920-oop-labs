class CheckResult:
    def __init__(self, name: str, passed: bool, message: str = ""):
        self.name = name
        self.passed = passed
        self.message = message

    def __repr__(self) -> str:
        status = "✅" if self.passed else "❌"
        return f"{status} {self.name}: {self.message}".strip()


def example_checks():
    """Very simple check, just to verify the library installed in Colab."""
    return [CheckResult("example", True, "Library installed correctly")]


def lab01_public_checks(bank_account_cls) -> list[CheckResult]:
    """
    Light, public safe checks for Lab 01.
    You will call this from the notebook with the student's BankAccount class.
    Do not put edge case tricks here. Save those for the private repo.
    """
    results: list[CheckResult] = []

    try:
        acc = bank_account_cls("Ada", 100)
        if getattr(acc, "balance", None) == 100:
            results.append(CheckResult("constructor sets balance", True))
        else:
            results.append(CheckResult("constructor sets balance", False, f"Got balance={getattr(acc, 'balance', None)}"))
    except Exception as e:
        results.append(CheckResult("constructor sets balance", False, f"Exception: {e}"))

    try:
        acc = bank_account_cls("Ada", 0)
        acc.deposit(50)
        if getattr(acc, "balance", None) == 50:
            results.append(CheckResult("deposit increases balance", True))
        else:
            results.append(CheckResult("deposit increases balance", False, f"Got balance={getattr(acc, 'balance', None)}"))
    except Exception as e:
        results.append(CheckResult("deposit increases balance", False, f"Exception: {e}"))

    return results
