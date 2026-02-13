**Subdomain:** ML

The standard self-attention mechanism in Transformers has quadratic time and space complexity with respect to sequence length, limiting its application to long sequences. Several approaches have been proposed to address this limitation through different approximation and optimization techniques.

Your goal is to analyze and compare three prominent efficient attention mechanisms using information available prior to January 28, 2026:

1. Identify the papers that introduced **Linformer**, **Performer (FAVOR+)**, and **FlashAttention**. For each paper, provide the title, first author, year of publication, and the venue or publication type (conference, journal, or preprint).

2. Compare the three approaches based on their complexity characteristics and approximation strategies. For each method, determine: (a) the time complexity as a function of sequence length n, (b) the space complexity as a function of sequence length n, (c) whether the method produces exact or approximate attention outputs, and (d) the core mathematical technique used (low-rank approximation, kernel methods, or algorithmic optimization). Create an image of a comparison table with four rows (time complexity, space complexity, exactness, technique) and four columns (parameter name, Linformer, Performer, FlashAttention). Title the table "Efficient Attention Mechanisms Comparison" and use markdown format.

3. Analyze the trade-offs between these approaches by addressing the following: Under what conditions would Linformer's low-rank assumption fail? What is the key limitation that prevents Performer from being used in all transformer applications despite its theoretical advantages? Why does FlashAttention achieve speedups despite having the same asymptotic complexity as standard attention? Your analysis should reference specific architectural constraints, mathematical properties, or implementation details mentioned in the papers.

## Citations

[1] Wang, S., Li, B. Z., Khabsa, M., Fang, H., & Ma, H. (2020). Linformer: Self-Attention with Linear Complexity. _arXiv preprint arXiv:2006.04768_. https://arxiv.org/abs/2006.04768

[2] Choromanski, K., Likhosherstov, V., Dohan, D., Song, X., Gane, A., Sarlos, T., ... & Weller, A. (2020). Rethinking Attention with Performers. _arXiv preprint arXiv:2009.14794_. https://arxiv.org/abs/2009.14794

[3] Dao, T., Fu, D. Y., Ermon, S., Rudra, A., & Ré, C. (2022). FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness. In _Advances in Neural Information Processing Systems_ (Vol. 35). https://arxiv.org/abs/2205.14135

[4] Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., ... & Polosukhin, I. (2017). Attention is all you need. In _Advances in Neural Information Processing Systems_ (Vol. 30). https://arxiv.org/abs/1706.03762
