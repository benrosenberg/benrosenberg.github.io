---
header-includes: |
    \usepackage[left=0.5in, right=0.5in, top=0.85in, bottom=0.85in]{geometry}
    \usepackage{multicol}
    \usepackage[most]{tcolorbox}
    \usepackage{graphicx}
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

\begin{center} \Large\textbf{Exam 2 Review Sheet} \end{center}

\begin{multicols}{2}

\begin{center} {\sc Regular operations and Regular expressions} \end{center}

\textbf{Regular operations} are the three operations that are applied to sets (for our purposes, those sets are languages $\Sigma$). 

They are as follows:

\begin{center}
\begin{tabular}{c|c|c}
    operation & symbol & what it does\\
    \hline
    \textbf{union} & $\cup$ & usual union set op. \\
    \textbf{concatenation} & $\circ$, $\cdot$, or none & glues strings together \\
    \textbf{Kleene star} & $\phantom{.}^*$ & zero or more of elt.
\end{tabular}
\end{center}

Let the number of elements in sets $A$ and $B$ be $|A|$ and $|B|$. Then:
\begin{itemize}
    \item The number of elements in $|A \cup B|$ is $|A| + |B| - |A\cap B| \leq |A| + |B|$
    \item The number of elements in $|A \circ B|$ is at most $|A|\times |B|$ (because concatenations are basically ordered pairs) but can be as low as $0$ if either $A$ or $B$ is $\varnothing$
    \item The number of elements in $|A^*|$ is either finite, in which case it is either $0$ (if $A = \varnothing$) or $1$ (if $A = \{\lambda\}$), or infinite, in which case it is $\aleph_0$
\end{itemize}

\textbf{Regular expressions} are strings made out of parentheses, the letters in $\Sigma$, and the symbols $\cup, \circ, *, \lambda, \varnothing$. They are made to represent a \textbf{regular language}, which is obtained by finitely many applications of regular expressions to the sets $\varnothing$, $\{\lambda\}$, and $\{i\}$ for all $i \in \Sigma$. This boils down to the fact that regular expressions are a shorthand for representing regular languages -- that is, languages that are defined by the three regular operations on some alphabet.

Examples (over $\Sigma = \{a,b,c\}$): 
\begin{itemize}
    \item Even length: $((a\cup b\cup c) (a\cup b\cup c))^*$
    \item Odd length: $((a\cup b\cup c) (a\cup b\cup c))^* (a\cup b\cup c)$
    \item Length $\leq 2$: $(a\cup b\cup c\cup \lambda) (a\cup b\cup c\cup \lambda)$
    \item Contains \texttt{abcb} or \texttt{bca}: $(a\cup b\cup c)^* (abcb\cup bca) (a\cup b\cup c)^*$
    \item Contains odd number of \texttt{a}'s: $((b\cup c)^*a(b\cup c)^*a(b\cup c)^*)^* a (b\cup c)^*$
    \item Contains as a substring both \texttt{abb} and \texttt{bca}: omitted for brevity (accounting for all ordering cases and overlaps makes it really long)
\end{itemize}

Theorem (proven in \textsf{NFA} part by Kleene's Thm. equivalence): If there is a regex for some language, there is a regex for its complement.

\begin{center} {\sc Context-free grammars and languages} \end{center}

A \textbf{context free grammar} is a structure defined as $G = (\Sigma, V, P, S)$ where $\Sigma$ is the usual kind of alphabet (set of letters), $V$ is the set of variables (also called an alphabet of variables) used in the grammar (which does not overlap with $\Sigma$: so, $V\cap \Sigma = \varnothing$), $S$ is the designated start symbol (note that $S\in V$ always, so $V\neq \varnothing$), and $P$ is the set of rules (``productions") for going from one variable to another variable or string. $P$ is a subset of $V\times (\Sigma \cup V)^*$ because we're going from $V$ to some number of elements of the intersection of $\Sigma$ and $V$. (Note further that $P$ is finite despite the fact that $|(\Sigma \cup V)^*| = \aleph_0$.)

We say that if $(A, w) \in P$, $A$ is a variable in $V$, and $w$ is some ``word" made of variables and letters and is in $(\Sigma \cup V)^*$. We can also write $(A,w)\in P$ as $A\rightarrow w$, spoken ``$A$ derives $w$".

If $A\rightarrow w_1$, and $A\rightarrow w_2$, $A\rightarrow \dots$ etc., we can write $A\rightarrow w_1 | w_2 | \dots$. 

Example CFG (1):
\begin{itemize}
    \item $G = (\Sigma, V, P, S)$
    \item $\Sigma = \{a,b,c\}$
    \item $S$ is the start state
    \item $V = \{S, A, B, D\}$
    \item $P :$
    \begin{itemize}
        \item $S \rightarrow AB|BD$
        \item $A\rightarrow aA|c$
        \item $B\rightarrow Bb|ca$
        \item $D\rightarrow abD|\lambda$
    \end{itemize}
\end{itemize}

The CFG operates as follows. Start with the start symbol $S$. Then, proceed to the next step, of $AB$ and $BD$ (recall that the pipe is the symbol for union and that the lack of space between, say, $AB$ and $BD$ is indicative of their concatenation). We continue substituting into variables with every possibility (with branching paths denoted by the union operators) until we have created every string possible from the CFG.

More formally, we say that a variable $E\in V$ \textbf{derives a sentence $w \in (\Sigma \cup V)^*$} in one step if $E\rightarrow w$ is in $P$. For example, $B$ derives the string $ca$ in one step. 

Then, inductively, we say that variable $E\in V$ derives a sentence $x\in (\Sigma \cup V)^*$ in $n+1$ steps if all of the following hold:

\begin{enumerate}
    \item $w$ derives some $y \in (\Sigma \cup V)^*$ in $n$ steps,
    \item $y$ is equal to some concatenation $y_1 F y_2$, where $y_1$ and $y_2$ are strings in $(\Sigma \cup V)^*$ and $F \in V$ is a variable,
    \item There is some rule $F \rightarrow y_0$ in $P$ for some string $y_0 \in (\Sigma \cup V)^*$, and
    \item The concatenation $y_1 y_0 y_2$ is equal to $x$.
\end{enumerate}

We can make context-free grammars for regular expressions using a couple constructs, which are associated with the regular operators of union, concatenation, and the Kleene star. We have already seen the union operation in the form of the pipe ($|$). The concatenation operation is simply denoted by putting two variables or letters or both next to each other. Finally, the Kleene star is described using the following examples:

Example: Turn the regular expression $a^*c$ into a CFG.

We can do this with the following (single) rule: $S \rightarrow aS|c$. This prepends zero or more $a$'s to the beginning of the string, and adds a $c$ to the end when it is done so that the string always ends in $c$. We can see that $A$ from example (1) is the same as this expression.

Similarly, from example (1), we can see that $B \rightarrow cab^*$ because we are appending zero or more $b$'s to the end of string $B$, which must begin with $ca$. $D$ must go to $(ab)^*$ because we are prepending $ab$ zero or more times to $D$, which must be ended by $\lambda$, the empty string.

Not every CFG needs to define a regular language. For example, the language $L = \{a^n b^n | n\geq 0\}$ cannot be defined by a regular expression. Two attempts might be $(ab)^*$ and $a^*b^*$, but in the first, we have $abab$ contained and in the second we have $aab$ contained, so neither work. The CFG for $L$ could be the usual (with $\Sigma = \{a,b\}$) with $P: S \rightarrow \lambda | aSb$. In this grammar we prepend an $a$ and append a $b$ the same number of times ($n$), which is in line with what we want from $L$.

A more complex example of this type might be the language $L = \{a^n ccb^{2n} | n\geq 0\}$. We say that this \emph{telescopes} as there are equivalent exponents at either end. In this example our rule is $S\rightarrow aSbb|cc$, as we prepend one $a$ for each two $b$'s we append, and have two $c$'s in the middle.

While not all languages generated by CFGs need to be regular, we can use the regular operations of union, concatenation, and the Kleene star on CFGs $G_1$ and/or $G_2$ to create a new CFG $G$ (the set of languages generated by context-free grammars is closed under the regular operations).

For the union operator $L(G_1) \cup L(G_2)$, we create a new start state $S$ separate from any of the states in $G_1$ or $G_2$ and add the new rule to $P$ that $S \rightarrow S_1 | S_2$.

For the concatenation operator $L(G_1)L(G_2)$, we create a new start state $S$ separate from any of the states in $G_1$ or $G_2$ and add the new rule to $P$ that $S \rightarrow S_1 S_2$.

For the Kleene star operator $L(G_1)^*$, we create a new start state $S$ separate from any of the states in $G_1$ and add the new rule to $P$ that $S \rightarrow \lambda | S S |S_1$. This rule tells us that $S$ can make zero or more copies of itself.

Next, we want to try turning regular expressions $e$ into CFGs (we know that we can't necessarily do the opposite from the above telescoping examples). We define our algorithm to do this recursively, with base cases of the letters $i \;\forall i\in \Sigma$, the empty string $\lambda$, and the empty language $\varnothing$, which are the zero-operator regular expressions. The CFG rules for these are as follows:
$$\begin{array}{r|l}
    \text{regex} & \text{rule}\\
    \hline
    i \; \forall i \in \Sigma & S \rightarrow i \\
    \lambda & S\rightarrow \lambda \\
    \varnothing & \text{no rules}
\end{array}$$

What we then do is split the regular expression $e$ up into CFG variables by operator precedence. We consider the example $e = ab^*(a\cup b)\cup (bc\cup a)^*$:
$$\underbrace{ a \underbrace{b^*}_D \underbrace{(a\cup b)}_E }_A \cup \underbrace{(\underbrace{bc\cup a}_F)^*}_B$$

This results in the following rules:

\begin{itemize}
    \item $S\rightarrow A|B$
    \item $A\rightarrow aDE$
    \item $D\rightarrow bD|\lambda$
    \item $E\rightarrow a|b$
    \item $B\rightarrow \lambda|BB|F$
    \item $F\rightarrow bc|a$
\end{itemize}

\begin{center} {\sc Deterministic finite automata} \end{center}

We define a \textbf{deterministic finite automaton} or \textsf{DFA} as a structure $M = (Q, \Sigma, \delta, q_0, F)$ where these elements are defined as follows:

\begin{center}
\begin{tabular}{r|l}
    thing & what it is\\
    \hline
    $\Sigma$ & alphabet as usual\\
    $Q$ & set of states, $\neq \varnothing$\\
    $q_0$ & initial state $\in Q$\\
    $F$ & accept states $\subseteq Q$\\
    $\delta$ & transition fct $(Q\times \Sigma) \rightarrow Q$
\end{tabular}
\end{center}

We write that $[q,a,p] \in \delta$ if there is a transition from $q$ to $p$ on the receipt of input $a$.

The \emph{configuration} of a \textsf{DFA} is a state-string pair $(q,w)$ with $q\in Q$ and $w\in \Sigma^*$. Here, $q$ is the current state and $w$ is the portion of the input string that has yet to be processed. We say that a \textsf{DFA} starts in the configuration $(q_0, w_0)$ where $w_0$ is the entire string that is to be processed. 

A configuration is \emph{terminal} if it is of the form $(t,\lambda)$ with $t\in Q$, and is \emph{accepting} if $t\in F$ and otherwise \emph{rejecting}.

We say that $L(M)$ is the set of exactly those strings that \textsf{DFA} $M$ accepts (take $M$ from the initial configuration to an accepting one).

We can write the transition function $\delta$ in two different ways. The first is a list of transitions, in a table like so:

$$\begin{array}{c|c|c}
    & a & b \\
    \hline
    q & p & p \\
    p & q & q 
\end{array}$$

But we can also write this with a \textbf{state transition diagram} as follows:

\begin{center}
\begin{tikzpicture}
    \node (q) [state, initial, initial text = {}] {$q$};
    \node (p) [state, accepting] at (2,0) {$p$};
    \path [-stealth]
        (q) edge [bend left] node [above] {\texttt{a,b}} (p)
        (p) edge [bend left] node [below] {\texttt{a,b}} (q);
\end{tikzpicture}
\end{center}

In the above diagram, the initial state is $q$, as can be seen by the arrow entering $q$ from the margin. There is one accepting state, $p$, which can be seen by the double circle around $p$. We can see that on either an $a$ or $b$, the automaton changes state. Since $p$ (the accepting state) is reached by any odd number of transitions of the automaton, we can see that this automaton accepts only those strings which have an odd number of characters (since it is a \textsf{DFA}, we know implicitly that this automaton's alphabet is $\Sigma = \{a,b\}$).

Recall the previously-stated (but not proven) theorem that there is always a regular expression for the complement of any given regular expression. We begin to lay the groundwork for our proof of this theorem with the fact that the complement of the language defined by a \textsf{DFA} is exceedingly easy to make a \textsf{DFA} for: all we do is change $F$ to be $Q\backslash F$ -- that is, we invert the accept states. (**Note that this is \emph{not} the same for \textsf{NFA}s!**)

The intersection of two \textsf{DFA}s is a little harder to implement, but it too can be written as a single \textsf{DFA}. We say that if $L_1$ is accepted by the usual $M_1$, and $L_2$ is accepted by the usual $M_2$, then their intersection $L_1\cap L_2$ is accepted by $M = ((Q_1\times Q_2), \Sigma, \delta, q_0= (q_1, q_2), (F_1\times F_2))$. Here, $\delta$ contains tuple $[(p, q), a, (s,t)]$ exactly when both $[p, a, s] \in \delta_1$ and $[q, a, t] \in \delta_2$. In essence, we have composite states, each of which is a pair of states, so that we simulate both machines at the same time. 

We can also simulate \emph{modular arithmetic} with \textsf{DFA}s. Consider the case in which we wanted to accept only those strings with length divisible by 3. Then, we might have the following:

\begin{center}
\begin{tikzpicture}
    \node (zero) [state, initial, initial text = {}, accepting] {zero};
    \node (one) [state] at (2,1) {one};
    \node (two) [state] at (2,-1) {two};
    \path [-stealth]
        (zero) edge node [above left] {\texttt{a,b,c}} (one)
        (one) edge node [right] {\texttt{a,b,c}} (two)
        (two) edge node [below left] {\texttt{a,b,c}} (zero);
\end{tikzpicture}
\end{center}

This automaton moves circularly with each transition, and only accepts when the number of transitions is zero mod 3. As such, it only accepts strings with length divisible by 3.

A more complex example is as follows. Construct a \textsf{DFA} to accept the set of strings for which $$2n_a + n_b - n_c + 3 = \alpha,$$ where $n_a, n_b$, and $n_c$ refer to the number of $a$'s, $b$'s, and $c$'s respectively, and $\alpha\mod 5$ is odd. 

We can do this as follows:

\begin{center}
\begin{tikzpicture}
    \node (0) [state] {0};
    \node (1) [state, accepting] at (2,1) {1};
    \node (2) [state] at (4, 0) {2};
    \node (3) [state, initial below, initial text = {start}, accepting] at (3,-2) {3};
    \node (4) [state] at (1,-2) {4};
    \path [-stealth]
        (0) edge [bend left] node [above left] {\texttt{b}} (1)
        (0) edge node [below] {\texttt{a}} (2)
        (0) edge [bend left] node [below left] {\texttt{c}} (4)
        (1) edge [bend left] node [above right] {\texttt{b}} (2)
        (1) edge node [left] {\texttt{a}} (3)
        (1) edge [bend left] node [above left] {\texttt{c}} (0)
        (2) edge [bend left] node [below right] {\texttt{b}} (3)
        (2) edge node [above left] {\texttt{a}} (4)
        (2) edge [bend left] node [above right] {\texttt{c}} (1)
        (3) edge [bend left] node [below] {\texttt{b}} (4)
        (3) edge node [above right] {\texttt{a}} (0)
        (3) edge [bend left] node [below right] {\texttt{c}} (2)
        (4) edge [bend left] node [below left] {\texttt{b}} (0)
        (4) edge node [above right] {\texttt{a}} (1)
        (4) edge [bend left] node [below] {\texttt{c}} (3);
\end{tikzpicture}
\end{center}

Here, the accept states are 1 and 3 because, mod 5, they are the odd remainders. Then, the initial state is 3, because we explicitly add 3 to the end of the expression for $\alpha$. Finally, the transitions come in the form of arithmetic mod 5 scaled by the coefficients of $n_a$, $n_b$, and $n_c$: we can see that each input of $a$ corresponds to a increase in 2, each input of $b$ corresponds to an increase of 1, and each input of $c$ corresponds to a decrease of 1.

We can, however, do more than arithmetic with \textsf{DFA}s: we can also make \textsf{DFA}s that correspond to the containing of a substring, or having a certain start or end, etcetera. Really, we can do anything with \textsf{DFA}s that we can with regexes and vice versa (we will prove this later with Kleene's Thm.). For example, here is a \textsf{DFA} that accepts strings that contain $bb$:

\begin{center}
\begin{tikzpicture}
    \node (start) [state, initial, initial text = {}] {$\;$};
    \node (b) [state] at (2,0) {b};
    \node (bb) [state, accepting] at (4,0) {bb};
    \path [-stealth]
        (start) edge [loop above] node [above right] {\texttt{a,c}} (start)
        (start) edge [bend left] node [above] {\texttt{b}} (b)
        (b) edge [bend left] node [below] {\texttt{a,c}} (start)
        (b) edge node [above] {\texttt{b}} (bb)
        (bb) edge [loop above] node [above right] {\texttt{a,b,c}} (bb);
\end{tikzpicture}
\end{center}

However, longer substrings require ever more complex \textsf{DFA}s. The \textsf{DFA} for the set of exactly those strings that contain $babbabbba$, for instance, is significantly more difficult to draw, requiring one node for each letter in the string and then an extra one for the start, as well as 10 different transitions back, not all of which are intuitive due to the requirement that we accept overlaps in substring-finding attempts. The idea of a \emph{non-deterministic finite automaton}, or \textsf{NFA}, will help us make this substring graph much easier to draw.


\begin{center} {\sc Non-deterministic finite automata} \end{center}

We define a \textbf{non-deterministic finite automaton} or \textsf{NFA} as a structure $M = (Q, \Sigma, \delta, q_0, F)$ (much like a \textsf{DFA}) where:

\begin{center}
\begin{tabular}{r|l}
    thing & what it is\\
    \hline
    $\Sigma$ & same as \textsf{DFA}s: alphabet as usual\\
    $Q$ & same as \textsf{DFA}s: set of states, $\neq \varnothing$\\
    $q_0$ & same as \textsf{DFA}s: initial state $\in Q$\\
    $F$ & same as \textsf{DFA}s: accept states $\subseteq Q$\\
    $\delta$ & transition fct $\delta : Q\times (\Sigma\cup \{\lambda\}) \rightarrow \mathcal{P}(Q)$
\end{tabular}
\end{center}

As can be seen above, the only difference lies in the transition function $\delta$: instead of going from a state-symbol pair to a single state, we can actually go from a state-symbol pair OR a state-$\lambda$ pair to any number of states in $Q$. In fact, since $\mathcal{P}(Q)$ includes $\varnothing$, we can even have our transition ``die", in which case it does not continue with evaluation. To conceptualize the idea that the automaton is at a set of states rather than a single state, we might say that it clones itself, or is operating in parallel universes, or is extending roots like a tree towards the water that is an accept state. 

The aforementioned state-$\lambda$ pair refers to the $\lambda$-transition: that is, the ability of a \textsf{NFA} to move without receiving input. Such transitions are marked on the state transition diagram with $\lambda$ appropriately.

It should also be noted that the \emph{non-deterministic} part of the \textsf{NFA} plays a big role in its operation. States in \textsf{NFA}s don't need to have a transition on every input in $\Sigma\cup \lambda$ -- they might only have one, or even none at all.

An \textsf{NFA} accepts an input string when any one (we can use the existential quantifier $\exists$ here) of its ``clones" reaches an accept state at end of the input string $w_0$.

Back to the substring example from the end of the \textsf{DFA} portion, we can quite easily make such a diagram with \textsf{NFA}s:

\begin{center}

\resizebox{\linewidth}{!}
{
\begin{tikzpicture}
    \node (start) [state, initial, initial text = {}] {$\;$};
    \node (1) [state] at (2,0) {1};
    \node (2) [state] at (4,0) {2};
    \node (3) [state] at (6,0) {3};
    \node (4) [state] at (8,0) {4};
    \node (5) [state] at (10,0) {5};
    \node (6) [state] at (12,0) {6};
    \node (7) [state] at (14,0) {7};
    \node (8) [state] at (16,0) {8};
    \node (9) [state, accepting] at (18,0) {9};
    \path [-stealth]
        (start) edge [loop above] node [above right] {\texttt{a,b}} (start)
        (start) edge node [above] {\texttt{b}} (1)
        (1) edge node [above] {\texttt{a}} (2)
        (2) edge node [above] {\texttt{b}} (3)
        (3) edge node [above] {\texttt{b}} (4)
        (4) edge node [above] {\texttt{a}} (5)
        (5) edge node [above] {\texttt{b}} (6)
        (6) edge node [above] {\texttt{b}} (7)
        (7) edge node [above] {\texttt{b}} (8)
        (8) edge node [above] {\texttt{a}} (9)
        (9) edge [loop above] node [above right] {\texttt{a,b}} (9);
\end{tikzpicture}
}

\end{center}

It's a little hard to see, but state (9) is the accept state for the above \textsf{NFA}.


\begin{center} {\sc Kleene's theorem} \end{center}

\textbf{Kleene's theorem} states that the classes of languages defined by regexes, \textsf{DFA}s, and \textsf{NFA}s are equivalent, and are called \textbf{regular languages}.

The following diagram illustrates the relationship the three have:

\begin{center}
\begin{tikzpicture}
    \node (nfa) [state] {\textsf{NFA}};
    \node (regex) [state] at (2,3) {regex};
    \node (dfa) [state] at (4,0) {\textsf{DFA}};
    \path [-stealth]
        (nfa) edge [bend left] node [left] {alg.} (regex)
        (regex) edge [bend left] node [above left] {alg.} (nfa)
        (nfa) edge [bend left] node [below] {alg.} (dfa)
        (dfa) edge [bend left] node [below] {special case} (nfa);
\end{tikzpicture}
\end{center}

``alg." here refers to the existence of an algorithm. Note that \textsf{DFA}s are a special case of \textsf{NFA}s, with no $\lambda$=transitions and determinism required.

There are three major algorithms insofar as these conversions are concerned, as can be seen by the above diagram's arrows, and one extra algorithm included below for the \textbf{application of regular operations to \textsf{DFA}s and \textsf{NFA}s}. We begin with this ``extra" algorithm.

For the purposes of the below three regular operation demonstrations, consider finite state automata $M_1$ and $M_2$ as defined by the state transition diagrams below:

\begin{center}
\begin{tikzpicture}
    \node (a1) [state, initial, initial text = {$M_1$ = }] {$\;$};
    \node (m1) [state, initial by diamond] at (2,0) {$M_1$};
    \node (a2) [state, accepting] at (4,0) {$\;$};
    \path [-stealth]
        (a1) edge node {$\;$} (m1)
        (m1) edge node {$\;$} (a2);
\end{tikzpicture}
\end{center}

\begin{center}
\begin{tikzpicture}
    \node (b1) [state, initial, initial text = {$M_2$ = }] {$\;$};
    \node (m2) [state, initial by diamond] at (2,0) {$M_2$};
    \node (b2) [state, accepting] at (4,0) {$\;$};
    \path [-stealth]
        (b1) edge node {$\;$} (m2)
        (m2) edge node {$\;$} (b2);
\end{tikzpicture}
\end{center}

The important takeaway here is that $M_1$ and $M_2$ have \emph{zero in-degree} initial states and \emph{zero out-degree} accepting states, which means that they don't have edges going into the initial state (except the one from space), and that they don't have any edges coming out of accepting states. It is important that you keep this in mind, as trying to use the below rules to apply regular operations to automata may result in faulty automata if the input automata are not of this form. (If they \emph{aren't} in this form, then we can put them into this form by adding artificial start and end nodes with $\lambda$-transitions.)

\textbf{Union} of $M_1\cup M_2$ of $M_1$ and $M_2$:

\begin{center}

\resizebox{\linewidth}{!}
{
\begin{tikzpicture}
    \node (start) [state, initial, initial text = {$M$ = }] {$\;$};
    \node (end) [state, accepting] at (8,0) {$\;$};

    \node (a1) [state] at (2, 1) {$\;$};
    \node (m1) [state, initial by diamond] at (4,1) {$M_1$};
    \node (a2) [state] at (6,1) {$\;$};
    \path [-stealth]
        (start) edge [above left] node {$\lambda$} (a1)
        (a1) edge node {$\;$} (m1)
        (m1) edge node {$\;$} (a2)
        (a2) edge [above right] node {$\lambda$} (end);

    \node (b1) [state] at (2, -1) {$\;$};
    \node (m2) [state, initial by diamond] at (4,-1) {$M_2$};
    \node (b2) [state] at (6,-1) {$\;$};
    \path [-stealth]
        (start) edge [below left] node {$\lambda$} (b1)
        (b1) edge node {$\;$} (m2)
        (m2) edge node {$\;$} (b2)
        (b2) edge [below right] node {$\lambda$} (end);
\end{tikzpicture}
}

\end{center}

\textbf{Concatenation} $M_1 M_2$ of $M_1$ and $M_2$:

\begin{center}

\resizebox{\linewidth}{!}
{
\begin{tikzpicture}
    \node (a1) [state, initial, initial text = {}] {$\;$};
    \node (m1) [state, initial by diamond] at (2,0) {$M_1$};
    \node (a2) [state] at (4,0) {$\;$};
    \path [-stealth]
        (a1) edge node {$\;$} (m1)
        (m1) edge node {$\;$} (a2);

    \node (b1) [state] at (6,0) {$\;$};
    \node (m2) [state, initial by diamond] at (8,0) {$M_2$};
    \node (b2) [state, accepting] at (10,0) {$\;$};
    \path [-stealth]
        (a2) edge [above] node {$\lambda$} (b1)
        (b1) edge node {$\;$} (m2)
        (m2) edge node {$\;$} (b2);
\end{tikzpicture}
}

\end{center}

\textbf{Kleene star} $M_1^*$ of $M_1$:

\begin{center}
\begin{tikzpicture}
    \node (a1) [state, initial, initial text = {}] {$\;$};
    \node (m1) [state, initial by diamond] at (2,0) {$M_1$};
    \node (a2) [state] at (4,0) {$\;$};
    \path [-stealth]
        (a1) edge node {$\;$} (m1)
        (a1) edge [bend left] node [above] {$\lambda$} (a2) 
        (m1) edge node {$\;$} (a2)
        (a2) edge [bend left] node [below] {$\lambda$} (a1);
\end{tikzpicture}
\end{center}

Now, onto the next algorithm, which is the \textbf{conversion of regular expressions into \textsf{DFA}s and \textsf{NFA}s}. 

We define the algorithm for conversion of regexes to finite state automata recursively, starting from the zero-operator regular expressions and then building around them. 

Recall that the zero-operator regular expressions are the letters in $\Sigma$, the empty string $\lambda$, and $\varnothing$. They become the following finite state automata:

\begin{center}
\begin{tikzpicture}
    \node (a1) [state, initial, initial text = {$a\implies$}] {$\;$};
    \node (m1) [state, accepting] at (2,0) {$\;$};
    \path [-stealth]
        (a1) edge node [above] {$a$} (m1);
\end{tikzpicture}

\begin{tikzpicture}
    \node (a1) [state, initial, initial text = {$\lambda\implies$}] {$\;$};
    \node (m1) [state, accepting] at (2,0) {$\;$};
    \path [-stealth]
        (a1) edge node [above] {$\lambda$} (m1);
\end{tikzpicture}

\begin{tikzpicture}
    \node (a1) [state, initial, initial text = {$\varnothing\implies$}] {$\;$};
    \node (m1) [state, accepting] at (2,0) {$\;$};
\end{tikzpicture}
\end{center}

From these base cases we can construct finite automata for all regular expressions. An example follows.

Example: Three different ways to write $(a\cup b)^*$

\begin{center}
\begin{tikzpicture}
    \node (p) [state, initial, initial text = {}] {$\;$};
    \path [-stealth]
        (p) edge [loop above] node [above right] {\texttt{a,b}} (p);
\end{tikzpicture}
\end{center}

\begin{center}
\begin{tikzpicture}
    \node (a) [state, initial, initial text = {}] {$\;$};
    \node (b) [state] at (2,0) {$\;$};
    \node (c) [state] at (4,0) {$\;$};
    \node (d) [state] at (6,0) {$\;$};
    \path [-stealth]
        (a) edge node [above] {$\lambda$} (b)
        (b) edge node [above] {\texttt{a,b}} (c)
        (b) edge [bend left] node [above] {$\lambda$} (c)
        (c) edge node [above] {$\lambda$} (d)
        (c) edge [bend left] node [below] {$\lambda$} (b);
\end{tikzpicture}
\end{center}

\begin{center}
\resizebox{\linewidth}{!}
{
\begin{tikzpicture}
    \node (a) [state, initial, initial text = {}] {$\;$};
    \node (b) [state] at (2,0) {$\;$};
    \node (c1) [state] at (4,2) {$\;$};
    \node (c2) [state] at (4,-2) {$\;$};
    \node (d1) [state] at (6,2) {$\;$};
    \node (d2) [state] at (6,-2) {$\;$};
    \node (e) [state] at (8,0) {$\;$};
    \node (f) [state] at (10,0) {$\;$};
    \path [-stealth]
        (a) edge node [above] {$\lambda$} (b)
        (b) edge node [above left] {$\lambda$} (c1)
        (b) edge node [below left] {$\lambda$} (c2)
        (b) edge [bend left] node [above] {$\lambda$} (e)
        (e) edge [bend left] node [above] {$\lambda$} (b)
        (c1) edge node [above] {\texttt{a}} (d1)
        (c2) edge node [below] {\texttt{b}} (d2)
        (d1) edge node [above right] {$\lambda$} (e)
        (d2) edge node [below right] {$\lambda$} (e)
        (e) edge node [above] {$\lambda$} (f);
\end{tikzpicture}
}
\end{center}

The next algorithm is for the \textbf{conversion between \textsf{NFA}s and \textsf{DFA}s}. The main idea here is that the states in the created \textsf{DFA} are each a set of states from the \textsf{NFA} (as would be implied by the transition function's codomain of $\mathcal{P}(Q)$). So, we first need to make some kind of table for the $\delta$ for the \textsf{NFA} with the states as the sets. 

Then, we need to understand the notion of $\lambda$-closure. The \textbf{$\lambda$-closure} of a state $x$ in an \textsf{NFA}, denoted $\mathcal{C}(x)$, is the set of states that are reachable by zero transitions (that is, the reading of the empty string $\lambda$) from the state. This becomes a recursive definition when we realize that multiple $\lambda$-transitions can be connected to each other. 

The reason $\lambda$-closure is important is that it is used in conjunction with the $\delta$ enumeration, used to ensure that we have actually enumerated all of the possible states that are transitioned to. 

We can write the \textsf{DFA} transition function as follows, for state $x$ and input $a$ as

$$\delta_\textsf{NFA}(x, a) = \mathcal{C}\Bigg(\bigcup_{p\in x} \delta_\textsf{DFA}(p,a)\Bigg).$$

The last algorithm is for the conversion from \textbf{finite automaton to regular expression}. To begin, we need to understand the notion of a \textbf{generalized expression graph} (GEG). We define a GEG as a graph (\emph{not} a finite automaton) with arcs labeled by regular expressions. (The definition of a graph is omitted here for brevity, and it is assumed that it has been covered in prerequisite material.) In terms of our previous knowledge, an \textsf{NFA} is a special case of a GEG, where the labels on the arc are either a single symbol or $\lambda$.

The main idea of this algorithm is to transform the original automaton, through a sequence of equivalent GEGs, until a trivial one is obtained, from which the resulting regular expression will be easily visible. This trivial GEG will be of the following form:

\begin{center}
\begin{tikzpicture}
    \node (a) [state, initial, initial text = {}] {$\;$};
    \node (b) [state, accepting] at (2,0) {$\;$};
    \path [-stealth]
        (a) edge node [above] {$e$} (b);
\end{tikzpicture}
\end{center}

Here, $e$ is our desired regular expression. We want to keep modifying the original \textsf{NFA} until we can get something of the above form, meaning that, for an \textsf{NFA} with $k$ nodes, we'll need to eliminate $k-2$ nodes.

Before starting this algorithm, we \emph{need to make the original automaton compliant}: that is, its initial and accept state need to have zero in- and out-degree respectively.

After we have made the automaton compliant, we need to make an adjacency matrix-like table, with each node on the rows and columns, and the transitions between them in the cells of the matrix. An example follows:

\begin{center}
\begin{tikzpicture}
    \node (1) [state, initial, initial text = {}] {1};
    \node (2) [state] at (2, 0) {2};
    \node (3) [state] at (4, 0) {3};
    \node (4) [state, accepting] at (6, 0) {4};
    \path [-stealth]
        (1) edge node [above] {$\lambda$} (2)
        (2) edge [loop above] node [above right] {$a$} (2)
        (2) edge [bend left] node [above] {$b$} (3)
        (3) edge [bend left] node [above] {$b$} (2)
        (3) edge [loop above] node [above right] {$a$} (3)
        (3) edge node [above] {$\lambda$} (4);
\end{tikzpicture}
\end{center}

We can see that the above \textsf{NFA} is a compliant automaton accepting strings with an odd number of $b$'s. This automaton can be represented by the following adjacency matrix-like table:

$$\begin{array}{c|c|c|c|c}
    & 1 & 2 & 3 & 4 \\
    \hline
    1 & \varnothing & \lambda & \varnothing & \varnothing \\
    \hline
    2 & \varnothing & a & b & \varnothing \\
    \hline
    3 & \varnothing & b & a & \lambda \\
    \hline
    4 & \varnothing & \varnothing & \varnothing & \varnothing 
\end{array}$$

We iteratively rewrite this table, until we are left with two nodes. Here is the first iteration:

$$\begin{array}{c|c|c|c}
    & 1 & 3 & 4 \\
    \hline
    1 & \varnothing & a^*b & \varnothing \\
    \hline
    3 & \varnothing & a \cup ba^*b & \lambda \\
    \hline
    4 & \varnothing & \varnothing & \varnothing
\end{array}$$

We are essentially reversing the regular operations from a previous algorithm in this section.

The final iteration:

$$\begin{array}{c|c|c}
    & 1 & 4 \\
    \hline
    1 & \varnothing & a^*b (a\cup b a^*b)^* \\
    \hline
    4 & \varnothing & \varnothing
\end{array}$$

So, we can see that the regular expression for an odd number of $b$'s is $a^*b (a\cup b a^*b)^*$.

\end{multicols}

\begin{center} \textbf{Exam on Monday. Good luck!} \end{center}
