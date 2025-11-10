class CheckResult:
    def __init__(self, name: str, passed: bool, message: str = ""):
        self.name = name
        self.passed = passed
        self.message = message

    def __repr__(self) -> str:
        status = "✅" if self.passed else "❌"
        return f"{status} {self.name}: {self.message}".strip()


def example_checks():
    return [CheckResult("example", True, "Library installed correctly")]


def lab01_public_checks(bank_account_cls):
    results = []

    # Constructor with owner and initial balance
    try:
        acc = bank_account_cls("Ada", 100)
        if getattr(acc, "balance", None) == 100:
            results.append(CheckResult("constructor sets balance", True))
        else:
            results.append(
                CheckResult(
                    "constructor sets balance",
                    False,
                    f"Expected balance 100, got {getattr(acc, 'balance', None)}",
                )
            )
    except Exception as e:
        results.append(
            CheckResult("constructor sets balance", False, f"Exception: {e}")
        )

    # Deposit
    try:
        acc = bank_account_cls("Ada", 0)
        acc.deposit(50)
        if getattr(acc, "balance", None) == 50:
            results.append(CheckResult("deposit increases balance", True))
        else:
            results.append(
                CheckResult(
                    "deposit increases balance",
                    False,
                    f"Expected balance 50, got {getattr(acc, 'balance', None)}",
                )
            )
    except Exception as e:
        results.append(
            CheckResult("deposit increases balance", False, f"Exception: {e}")
        )

    # Withdraw
    try:
        acc = bank_account_cls("Ada", 100)
        acc.withdraw(40)
        if getattr(acc, "balance", None) == 60:
            results.append(CheckResult("withdraw decreases balance", True))
        else:
            results.append(
                CheckResult(
                    "withdraw decreases balance",
                    False,
                    f"Expected balance 60, got {getattr(acc, 'balance', None)}",
                )
            )
    except Exception as e:
        results.append(
            CheckResult("withdraw decreases balance", False, f"Exception: {e}")
        )

    return results
