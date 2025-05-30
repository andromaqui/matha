# Programming Language Architecture Guide

## Overview

This guide explains the fundamental architecture that almost every programming language follows. Understanding this pipeline is crucial for building your own language (like Matha for inverse problems).

## The Standard Pipeline

```
Source Code → Lexer → Parser → AST → Interpreter/Compiler → Execution
```

## Pipeline Stages

### 1. Source Code
- **Input**: Raw text from source files
- **Example**: `"x = 42 + 7\nprint x"`
- **Purpose**: The human-readable code that needs to be processed

### 2. Lexer (Tokenizer)
- **Input**: Raw source code string
- **Output**: Stream of tokens
- **Purpose**: Breaks text into meaningful chunks (tokens)
- **Example**: 
  ```
  Input:  "x = 42 + 7"
  Output: [IDENTIFIER('x'), EQUALS, NUMBER(42), PLUS, NUMBER(7)]
  ```

### 3. Parser
- **Input**: Stream of tokens from lexer
- **Output**: Abstract Syntax Tree (AST)
- **Purpose**: Understands the structure and grammar of the language
- **Process**: Uses grammar rules to build a tree representation

### 4. Abstract Syntax Tree (AST)
- **Structure**: Tree representation of program structure
- **Example**:
  ```
  Program
  ├── Assignment
  │   ├── Variable: 'x'
  │   └── BinaryOp: '+'
  │       ├── Number: 42
  │       └── Number: 7
  └── Print
      └── Variable: 'x'
  ```

### 5. Interpreter/Compiler
- **Interpreter**: Walks AST and executes directly
- **Compiler**: Translates AST to machine code or bytecode
- **Runtime Environment**: Manages variables, memory, function calls

### 6. Execution/Output
- **Result**: Program runs and produces output
- **Example**: Console displays `49`

## Language Categories

### By Execution Model
- **Compiled**: Translated to machine code before running (C, Rust, Go)
- **Interpreted**: Executed line-by-line at runtime (Python, JavaScript, Ruby)
- **Hybrid**: Compiled to bytecode, then interpreted (Java, C#)

### By Programming Paradigms
- **Imperative**: Step-by-step instructions (C, Python)
- **Functional**: Functions as first-class citizens, immutability (Haskell, Lisp)
- **Object-Oriented**: Everything is objects with methods (Java, C++)
- **Logic**: Declare facts and rules, let system find solutions (Prolog)
- **Declarative**: Say what you want, not how to get it (SQL, HTML)

### By Type Systems
- **Static**: Types checked at compile time (C++, Java, Rust)
- **Dynamic**: Types checked at runtime (Python, JavaScript)
- **Strong**: Strict type enforcement (Python, Java)
- **Weak**: Loose type conversion (C, JavaScript)

### By Memory Management
- **Manual**: Programmer manages memory (C, C++)
- **Garbage Collected**: Automatic memory cleanup (Java, Python)
- **Reference Counted**: Track object usage (Swift, Python uses both)

### By Domain
- **General Purpose**: Good for many tasks (Python, Java)
- **Domain-Specific**: Specialized for specific problems (SQL, R, MATLAB)

## Building Your Language (Matha)

### Approach for Matha
- **Type**: Domain-Specific Language (DSL) for inverse problems
- **Execution**: Interpreted (for rapid prototyping)
- **Paradigm**: Imperative with functional features
- **Type System**: Dynamic (initially)

### Questions to Explore:

What language features best support inverse problem solving?
How can type systems capture mathematical constraints?
What compiler optimizations are domain-specific?
How does language design affect numerical stability?