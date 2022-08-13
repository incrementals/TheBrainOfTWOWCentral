from typing import List, Dict, Union

import discord

from src.interpreter.userfunction import UserFunction


class Codebase:
    def __init__(self, lines, user, arguments):
        self.lines: List[str] = lines
        self.variables: List[Dict[str, str]] = [{}]
        self.functions: Dict[str, UserFunction] = {}
        self.user: Union[discord.User, None] = user
        self.arguments: Union[List[str], None] = arguments
        self.output: str = ""

        # TODO: This is temporary while s3.py gets revamped in 1.1
        self.global_limit: int = 0
        self.ret = None
        self.sendpm = False
        self.pmoutput: str = ""
        self.giveToBot = {}
