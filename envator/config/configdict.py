from __future__ import annotations

import re

from envator.util.namingcase import NamingCase


class EnvatorConfigDict(dict):
    def with_keys_case(self, case: NamingCase) -> EnvatorConfigDict:
        if case == NamingCase.LOWER:
            return {k.lower(): v for k, v in self.items()}
        if case == NamingCase.UPPER:
            return {k.upper(): v for k, v in self.items()}
        elif case == NamingCase.SNAKE:
            return {re.sub(r"(?<!^)(?=[A-Z])", "_", k).lower(): v for k, v in self.items()}
        elif case == NamingCase.KEBAB:
            return {re.sub(r"(?<!^)(?=[A-Z])", "-", k).lower(): v for k, v in self.items()}
        elif case == NamingCase.TITLE:
            return {k.title(): v for k, v in self.items()}
        elif case == NamingCase.CAMEL:
            result = {}
            for k, v in self.items():
                tmp = re.sub(r"(_|-)+", " ", k).title().replace(" ", "")
                if len(tmp) == 0:
                    continue
                if str(k[0]).islower():
                    tmp = str(tmp[0]).lower() + tmp[1:]
                result[tmp] = v
            return result
        elif case == NamingCase.PASCAL:
            return {"".join(x.capitalize() for x in k.split("_")): v for k, v in self.items()}
        else:
            raise ValueError(f"Invalid naming case '{case}'")
