"""
Sean Ross Ross wrote a new branch of Block Context that relies on a few improvements
 - The parser for the code blocks is AST instead of the deprecated compiler module
 - The code blocks are not necessarily assumed to be 1-liners with acyclic tree dependencies
 - The code blocks are written in a new smart_code object that is a lot lighter weight than Block.
To use and combine them, another object called lego was written.

 This new branch is called new_block in the ETS - Codetools project
"""


# This describes the old APIIn [2]: from codetools.blocks.block import Block

In [3]: block = Block("""
   ...: a = b
   ...: c = a + 22
   ...: """)

In [4]: block.inputs
Out[4]: set(['b'])

In [6]: block.outputs
Out[6]: set(['a', 'c'])

In [7]: block.codestring
Out[7]: '\na = b\nc = a + 22\n'

In [8]: print block.codestring

a = b
c = a + 22

In [10]: print block.restrict(outputs = 'c').codestring
a = b
c = a+22


In [11]: print block.restrict(outputs = 'a').codestring
a = b


In [12]: block2 = Block("""
   ....: a[:] = 1
   ....: b = a*2
   ....: """)

In [13]: block.inputs
Out[13]: set(['b'])

In [14]: block.outputs
Out[14]: set(['a', 'c'])

In [15]: block2.outputs
Out[15]: set(['b'])

In [16]: block2.inputs
Out[16]: set(['a'])

In [17]: Block([block,block2])
Out[17]: Block(uuid=075cd01d-2d8f-4e6c-9af2-fc11756c409d)

In [18]: print Block([block,block2]).codestring
a = b
c = a+22
a[:] = 1
b = a*2
