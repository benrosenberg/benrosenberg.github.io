---
header-includes: |
    \usepackage[left=0.5in, right=0.5in, top=0.85in, bottom=0.85in]{geometry}
    \usepackage{multicol}
    \usepackage[most]{tcolorbox}
    \usepackage{tikz}
    \usetikzlibrary{automata, arrows.meta, positioning, shapes}
    \usepackage{fancyhdr}
    \pagestyle{fancy}
    \lhead{Ben Rosenberg}
    \chead{CSCI 320: Theory of Computation}
    \rhead{\today}
    \lfoot{Queens College}
    \cfoot{\thepage}
    \rfoot{Professor Bojana Obreni\'c}
---

\begin{center} \Large\textbf{Exam 1 Review Sheet} \end{center}

\begin{multicols}{2}

\begin{center} {\sc Predicates, Sets, Quantified formulae} \end{center}

Logical operators and their meanings:
$$\begin{array}{c|c|c}
    \text{operator} & \text{meaning} & \text{\texttt{true} when...} \\
    \hline
    p \land q & p \text{ and } q & \text{both $p$ and $q$ are true} \\
    p \lor q & p \text{ or } q & \text{one of $p$ or $q$ is true}\\
    p \implies q & p \text{ implies } q & \text{always unless \texttt{T} implies \texttt{F}}\\
    p \iff q & p \text{ iff } q,\; p \text{ equals } q & \text{$p$ and $q$ are the same} \\
    \neg p & \text{not } p & \text{$p$ is false}
\end{array}$$

Relevant logical operator facts:

\begin{itemize}
    \item DeMorgan's Laws: $\neg (p \land q) = (\neg p) \lor (\neg q)$, and $\neg(p\lor q) = (\neg p) \land (\neg q)$
    \item $(p \iff q) = (p \implies q) \land (q\implies p)$
    \item $p\implies q = \neg p \lor q$
\end{itemize}

A \textbf{proposition} is either \texttt{true} or \texttt{false}.

A \textbf{predicate} is a function that produces propositions, and depends on one or more variables over a domain.

\textbf{Quantifiers} and their meanings:
$$\begin{array}{c|l}
    \text{quantifier} & \text{\texttt{true} when...} \\
    \hline
    (\forall x)(P(x)) & \text{$P(x)$ is true for all $x$ in the domain} \\
    (\exists x)(P(x)) & \text{$P(x)$ is true for some $x$ in the domain}
\end{array}$$

Quantifiers bind variables to turn what would originally be a predicate into a proposition (or a predicate in one fewer variable).

A \textbf{set} is something that formalizes the notion of items which result in a predicate returning true. We say that for a set defined $S = \{x | P_S(x)\}$, the elements in $S$ are all $x$ for which $P_S(x)$ is true.

Set notation and its meaning:
$$\begin{array}{c|l}
    \text{notation} & \text{meaning} \\
    \hline
    x\in S & \text{$x$ is in set $S$} \\
    x\not\in S & \text{$x$ is not in set $S$}\\
    S\subseteq A & \text{$S$ is a \textbf{subset} of $A$} \\
    S\subset A & \text{$S$ is a \textbf{proper subset} of $A$} \\
    A\cup B & \text{\textbf{union} of $A$ and $B$} \\
    A \cap B & \text{\textbf{intersection} of $A$ and $B$} \\
    A \backslash B & \text{\textbf{set difference} of $A$ and $B$} \\
    \overline{A} & \text{\textbf{complement} of $A$} \\
    \varnothing & \text{the \textbf{empty set}} \\
    E & \text{the \textbf{universe} set} \\
    A\times B & \text{the \textbf{set product} of $A$ and $B$} \\
    \mathcal{P}(A) & \text{the \textbf{power set} of $A$} 
\end{array}$$

Definitions for set notation:

\begin{tabular}{c|l}
    thing & what it means \\
    \hline
    $A$ subset $B$ & all elements of $A$ are in $B$ \\
    $A$ proper subset $B$ & subset but $A\neq B$ \\
    $A$ union $B$ & all elements that are in $A$ and $B$ \\
    $A$ intersection $B$ & elements that are in both $A$ and $B$ \\
    set diff of $A$ and $B$ & elements in $A$ that are not in $B$ \\
    $A$ complement & elements in $E$ that are not in $A$ \\
    empty set $\varnothing$ & set with no elements in it \\
    universe set $E$ & set with every element in the domain \\
    product $A\times B$ & ordered pairs $(x,y) : x\in A, y\in B$ \\
    power set $\mathcal{P}(A)$ & set of all subsets of $A$
\end{tabular}

The \textbf{cardinality} of a set is its size (number of elements) for finite sets, and... \emph{basically} its size (but not quite) for infinite sets. 

The cardinality of the power set of set $A$, $|\mathcal{P}(A)| = 2^{|A|}$. 

\begin{center} {\sc Products, Relations, Functions (injective and surjective), Induction and Recursion, Alphabets and Strings} \end{center}

Products: see above (set product/Cartesian product, presumably).

A \textbf{function} $f : A\rightarrow B$ is a mapping from $A$ to $B$ that is in essence a subset of the set product of $A$ and $B$ (in other words, $f \subset A\times B$) in that it is a bunch of ordered pairs specifying which element of $A$ goes to which element of $B$. For general functions, we used the analogy of the gradebook as a function from students to grades.

Important function properties:
\begin{itemize}
    \item For all elements $a\in A$, there is an element $b\in B$ that gets mapped to by $f$ (in other words, $\forall a\in A \exists b \in B : f(a) = b$)
    \item $A$ is the domain of $f$ and $B$ is the target or codomain of $f$
    \item Every element in the domain has only one image/element that it is mapped to -- if $a$ has two images under $f$, then they must be equal to each other (the image is unique)
\end{itemize}

Ways to describe an input to $f$ and its output:
\begin{itemize}
    \item $f$ sends $x$ to $y$
    \item $(x,y) \in f$
    \item $f(x) = y$
    \item $f : x \mapsto y$
\end{itemize}

The \textbf{range} of a function is the set of values in its codomain that it actually maps elements in its domain to.

An \textbf{injective} function (also called one-to-one) is one for which each element in the range is mapped to by only one element in the domain. In the line-drawing analogy from class, we might think of it as prohibiting elements in the codomain from having more than one line drawn to them from the domain. We used the parking lot analogy for this in class.

A \textbf{surjective function} is one for which every output is mapped to by an input. (Probably not on the exam, as we didn't go over them in class.)

The \textbf{inverse} $f^{-1}$ of a function $f$ essentially switches the ordering of the ordered pairs from $f$. It maps from the range of $f$ to the domain of $f$. (Note that it can't necessarily map from the codomain to the domain as it's possible that not every element of the codomain was used by $f$.) We call $f^{-1}$ the \emph{partial inverse function}. 

A \textbf{partial function} is a function $f : S \rightarrow A$ where $S\subseteq A$. In other words, it is a function whose domain is a subset of its codomain. If some element $x$ is in the codomain but not the domain of $f$, we say that $f(x)$ is \emph{undefined}.

A \textbf{relation} is basically a generalized function that doesn't have the restriction that one input cannot map to multiple outputs. (Probably not on the exam, as we didn't go over them in class.)

A \textbf{total} function is one for which the domain is the same set as the codomain.

An \textbf{alphabet} is any \emph{finite} set, typically denoted (e.g.) $\Sigma = \{\texttt{a, b, c}\}$.

A \textbf{letter} is an element of an alphabet, e.g. \texttt{a} or \texttt{b}.

A \textbf{string} is any \emph{finite} sequence of letters. An example from the above alphabet might be \texttt{ababba}.

The \textbf{length} of a string is the number of letters in the string, denoted $|s|$ for string $s$.

The \textbf{empty string}, denoted $\lambda$, is the string without any letters in it. We say that $|\lambda| = 0$.

The concatenation of strings $x$ and $y$, denoted $x\circ y$ or $x\cdot y$, is $xy$ ($x$ written next to $y$). Ex. for $x = \texttt{abca}$, $y = \texttt{bac}$, $x\circ y = \texttt{abcabac}$ and $|x\circ y| = |x| + |y| = 4 + 3 = 7$.

A \textbf{language} is any set of strings (over the given alphabet). A language is always \emph{infinite} (consider concatenating $n$ letters, starting from $n=0$ which gives $\lambda$ and continuing. There is an injection from each of these $n$-letter strings to the natural numbers $\mathbb{N}$).

\textbf{Induction} is one method of proving things, but will not be explored too much. \emph{We won't ever have to write an inductive proof for something} -- it's enough to just know the reasoning behind it. It boils down to a base case and an inductive hypothesis. 

Ex. Consider a ladder with (countably) infinite rungs, and we want to show that we can climb to any rung. Induction allows us to say that if we can climb to the first rung (base case), and if we're at any rung, we can climb to the next rung on the ladder (inductive hypothesis), we can climb to any of the rungs on the ladder. 

Anyone reading this should already be familiar with \textbf{recursion} from coding such functions in their previous CS classes, but it doesn't really matter anyway because we didn't explicitly go over it in class. Induction uses a kind of recursion which is probably as much as you need to know for the exam (if anything).

\begin{center} {\sc Cardinalities, the natural numbers $\mathbb{N}$, Countable and Uncountable sets, Counting $\bigcup_{k=1}^\infty \mathbb{N}^k$} \end{center}

More precise definition of \textbf{cardinality}: We say that $|A|$ is the cardinality of a set $A$. Given two sets $A$ and $B$, if $|A| \leq |B|$, there exists some injective function from $A$ to $B$. With our parking lot idea, $A$ is the set of cars and $B$ is the set of parking spots. If $|A| = |B|$, then there are injections from $A$ to $B$ and from $B$ to $A$. If $|A| < |B|$ then there is an injection from $A$ to $B$ but \emph{not} from $B$ to $A$.

A set $A$ has \textbf{infinite cardinality} if there is some proper subset $S\subset A$ of $A$ with the same cardinality $|S| = |A|$ (there are injections between the two sets $S$ and $A$). 

The set $\mathbb{N} = \{0,1,2,3,\dots\}$ of \textbf{natural numbers} is infinite.

A set $A$ is \textbf{finite} if its cardinality $|A|$ is strictly less than $\aleph_0 = |\mathbb{N}|$.

A set is \textbf{countable} if its cardinality is not greater than $\aleph_0$. Otherwise, it is \textbf{uncountable}. In other words, a set is countable if it is either finite or has cardinality $\aleph_0$ (is countably infinite).

The \textbf{G\"odel injection} is one of our "failed attempts to construct an uncountable set." It essentially allows us to write any $k$-tuple of natural numbers as another natural number in $\mathbb{N}$. It is defined as $\mathcal{G} : \bigcup_{k=1}^\infty \mathbb{N}^k \rightarrow \mathbb{N}$. 

Fancily typeset, this is: $$\mathcal{G} : \underbrace{\mathbb{N}\times\mathbb{N}\times \cdots \times \mathbb{N}}_{k\;\text{times}}\rightarrow \mathbb{N}$$

The way we achieve this injection is with prime factorization. Any $k$-tuple, written $\langle x_1, x_2, \dots, x_k \rangle$, gets mapped to a natural number as follows: $$\mathcal{G}(\langle x_1, x_2, \dots, x_k \rangle) = p_1^{x_1 + 1} \cdot p_2^{x_2 + 1} \cdot \dots \cdot p_k^{x_k + 1},$$ where $p_i$ represents the $i$th prime number. 

Examples of \textbf{computing G\"odel numbers}:

\begin{itemize}
    \item $[1] \rightarrow 2^{1+1} = 2^2 = 4$
    \item $[1, 0] \rightarrow 2^{1 + 1} \cdot 3^{0 + 1} = 12$
    \item $[1, 0, 0] \rightarrow 2^{1 + 1} \cdot 3^{0 + 1} \cdot 5^{0 + 1} = 60$
\end{itemize}

Examples of \textbf{inverse G\"odel numbering}:

\begin{itemize}
    \item $\mathcal{G}^{-1}(2) = [0]$ because its prime factorization is $2^1$ which corresponds to $2^{0 + 1}$ and therefore the sequence containing only one 0
    \item $\mathcal{G}^{-1}(4480) = \texttt{undefined}$ because its prime factors do not cover consecutive primes (2, 3, 5, etc.) starting from 2 (without doing all the math it looks like it's missing a 3)
    \item $\mathcal{G}^{-1}(720) = [3,1,0]$ because 720's prime factorization is $2^4\cdot 3^2 \cdot 5^1$ which corresponds to $2^{3 + 1}\cdot 3^{1 + 1} \cdot 5^{0 + 1}$ and therefore $[3,1,0]$
\end{itemize}

Other questions about G\"odel numbering can be in the form of being given some tuple of variables, and being told various things about it, and using the properties of the numbering system to deduce things about the tuple's corresponding G\"odel number. Look at the class notes (\texttt{4.pdf}, page 5) for more examples.

\begin{center} {\sc Diagonalization proof that $|\{f : \mathbb{N} \rightarrow \{0,1\}\}|>\aleph_0$, Partial Functions} \end{center}

Partial functions: see above, by {\sc Functions}.

The \textbf{diagonalization proof} that $\mathcal{P}(\mathbb{N})$ is uncountable follows.

Assume for the sake of contradiction that there is some injection from the natural numbers $\mathbb{N}$ to its power set $\mathcal{P}(\mathbb{N})$. Then, we can write this injection as a table like so (the actual contents of the below table are irrelevant, they are just sequences of bits):

$$\begin{array}{c|l}
    & \texttt{0 1 2 3 4 5 6 }\dots \\
    \hline
    f_0 & \texttt{0 0 0 0 0 0 0}\dots \\
    f_1 & \texttt{1 0 0 0 1 0 0}\dots \\
    f_2 & \texttt{0 0 1 0 0 0 0}\dots \\
    f_3 & \texttt{1 1 1 1 1 1 1}\dots \\
    f_4 & \texttt{0 1 0 1 0 1 0}\dots \\
    \vdots & \, \vdots \;\;\,\, \vdots \;\;\,\, \vdots \;\;\,\, \vdots \;\;\,\, \vdots \;\;\,\, \vdots \;\;\,\, \ddots 
\end{array}$$

Here, each \texttt{0} or \texttt{1} represents whether the natural number in the top row is contained or not contained in $f_i$, each of which is a subset of $\mathbb{N}$. The table should list all of the infinite subsets of $\mathbb{N}$ in this way. Then, the argument against this construction proceeds as follows. Take a subset $D$ of $\mathbb{N}$, such that $n\in D \iff n\not\in f_n$. In other words, $D$ is the subset of $\mathbb{N}$ created by flipping each of the elements (from \texttt{0} to \texttt{1} or \texttt{1} to \texttt{0}) along the diagonal. Then, since $D$ is a subset of $\mathbb{N}$, it must have its own row in the table, which we will call number $\alpha$. So, $D = f_\alpha$. 

This, however, leads to a contradiction. If $\alpha \in D$ (the $\alpha$th bit in $D$ is a \texttt{1}), then $\alpha \not\in f_\alpha$ by our definition of $D$ as the subset created by flipping all the bits along the diagonal. But then, by the definition of $\alpha$ as the row to which $D$ is assigned (we said that $D = f_\alpha$), $\alpha\not\in D$ (the $\alpha$th bit in $D$ is a \texttt{0}). This is a contradiction.

The same occurs when we try to assume $\alpha \not\in D$. If $\alpha\not\in D$, then it must be in $f_\alpha$ by the definition of $D$ (as it was flipped on the diagonal). But since $D = f_\alpha$ by the definition of $\alpha$, $\alpha$ must be in $D$ and therefore we have the same contradiction.

So, we have proven by contradiction that $\mathbb{P}(\mathbb{N})$ is uncountable and thus that $|\mathcal{P}(\mathbb{N})| > \aleph_0$. \begin{flushright} $\square$ \end{flushright}

\end{multicols}

\begin{center} \textbf{Exam on Monday. Good luck!} \end{center}
