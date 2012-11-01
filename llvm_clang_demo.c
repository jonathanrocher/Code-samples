/* This test file is used to demo how to compile C down to the LLVM Intermediate 
Representation (LLVM-IR). To do so compile it with 
clang llvm_clang_demo.c -c -emit-llvm -S -o llvm_clang_demo.ll
*/

int foo(int a, int b)
{
  return a+b;
}
