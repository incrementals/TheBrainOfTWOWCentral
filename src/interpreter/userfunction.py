from typing import List, Dict


class UserFunction:
    def __init__(self, name: str, args: Dict[int, str], block: List[str], global_func: bool, codebase):
        self.args = args
        self.block = block
        self.codebase = codebase

        codebase.functions[name] = self

        # if global_func is True:

    def run(self, args: List[str]):
        print(f"{args} > {self.args} > {self.block} > {self.block[0]} > {self.block[0][0]}")

        # if len(block_buffer) > 1:
        #     main_buffer.append(block_buffer)
        # else:
        #     main_buffer.append(block_buffer[0])
        return self.enumerateList(*self.block, args)

    def enumerateList(self, block: List[str], args: List[str]):
        block_buffer = []
        for part in block:
            # recursion moment
            if isinstance(part, list):
                block_buffer.append(self.enumerateList(part, args))

            isarg = False
            for i, argument in self.args.items():
                if part == argument:
                    isarg = True
                    block_buffer.append(args[i])
            if not isarg:
                block_buffer.append(part)
        return block_buffer
