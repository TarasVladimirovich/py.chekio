from abc import ABC, abstractmethod
import re


class Rule(ABC):
    @abstractmethod
    def name(self) -> str:
        """Provides a name of the rule (like FP005)."""
        pass

    @abstractmethod
    def matches(self, line: str) -> bool:
        """Returns True if a given line matches the filter, otherwise, returns False."""
        pass


class FP001(Rule):
    def name(self):
        return 'FP001'

    def matches(self, line: str) -> bool:
        return line.rstrip().endswith('.')


class FP002(Rule):
    def name(self):
        return 'FP002'

    def matches(self, line: str) -> bool:
        return len(line) >= 100


class FP003(Rule):
    def name(self):
        return 'FP003'

    def matches(self, line: str) -> bool:
        return line.lower().count('a') >= 5


class FN201(Rule):
    def name(self):
        return 'FN201'

    def matches(self, line: str) -> bool:
        return line.lower().count('z') >= 3


class FN202(Rule):
    def name(self):
        return 'FN202'

    def matches(self, line: str) -> bool:
        return not bool(line)


class FN203(Rule):
    def name(self):
        return 'FN203'

    def matches(self, line: str) -> bool:
        return re.search('[a-zA-Z]', line) is None


class Mode:

    def __init__(self, path, rules):
        self.path = path
        self.rules = rules

    def do(self):
        with open(self.path, 'r') as file:
            line = file.readline()
            count = 1
            while line:
                if str(self.__class__.__name__).lower() == 'filter':
                    for rule in self.rules:
                        if rule.matches(line):
                            print(line, end='')
                            break
                else:
                    print(f'{count:>2}: ', end=' ')
                    for rule in rules:
                        if rule.matches(line):
                            print(rule.name(), end=' ')
                    print()
                    count += 1
                line = file.readline()

    def __str__(self):
        return str(self.__class__.__name__)


class Filter(Mode):
    pass


class Annotate(Mode):
    pass


if __name__ == "__main__":
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

    parser = ArgumentParser(
        description="A crazy file linter.",
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "mode",
        type=str,
        help="Choose what to do with a file",
        choices=["filter", "annotate"],
    )
    parser.add_argument(
        "path", type=str, help="a full or relative path to a file",
    )
    arguments = parser.parse_args()
    #vars(arguments)
    rules = [FP001(), FP002(), FP003(), FN201(), FN202(), FN203()]
    if arguments.mode == 'filter':
        mode = Filter(arguments.path, rules)
    else:
        mode = Annotate(arguments.path, rules)
    Mode.do(mode)
