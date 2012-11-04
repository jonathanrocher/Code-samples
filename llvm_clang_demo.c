/* This test file is used to demo how to compile C down to the LLVM Intermediate 
Representation (LLVM-IR). To do so compile it with 
$ clang llvm_clang_demo.c -c -emit-llvm -S -o llvm_clang_demo.ll
   -c for just compiling
   -S to generate a human readable file instead of binary bytecode

Look at the resulting ll file and look at it again once it has been simplified 
with the LLVM optimizer :
$ opt-3.0 -S -O3 llvm_clang_demo.ll
generates a simplified llvm byte code:

; ModuleID = 'llvm_clang_demo.ll'
target datalayout = "e-p:64:64:64-i1:8:8-i8:8:8-i16:16:16-i32:32:32-i64:64:64-f32:32:32-f64:64:64-v64:64:64-v128:128:128-a0:0:64-s0:64:64-f80:128:128-n8:16:32:64-S128"
target triple = "x86_64-pc-linux-gnu"

define i32 @foo(i32 %a, i32 %b) nounwind uwtable readnone {
  %1 = add nsw i32 %b, %a
  ret i32 %1
}
 
*/

int foo(int a, int b)
{
  return a+b;
}
