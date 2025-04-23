Feynman diagrams are used to compute correlation functions perturbitively.
A correlation function is the probably of observing a specific quantum state at later time "t" when starting from a specific quantum state at earlier time "t".
The way you do this is compute <ψ|(time propagation)|ψ>. Naively, we just use the time propagation operator exp(-i*integration(H, dt)*t), but when we expand in a power series,
we need to time-order the H's for which you use Wick's theorem. Then the correlation function for each term in the time-ordered expansion is pictorially represented by a Feynman diagram.
