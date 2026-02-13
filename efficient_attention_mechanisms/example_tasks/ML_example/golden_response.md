Summarizing protein relationships used for next sentence prediction-based training in paired input protein language models

Locating relevant papers
The supplied starting paired-input protein language model (pLM) models were PLUS-RNN (Pre-Training of Deep Bidirectional Protein Sequence Representations With Structural Information) [1], NABP-BERT (NABP-BERT: NANOBODY®️-antigen binding prediction based on bidirectional encoder representations from transformers (BERT) architecture) [2], and PLM-Interact (PLM-interact: extending protein language models to predict protein-protein interactions) [3]. None of the papers cite other works which they claim also describe paired input pLM models with NSP-like training tasks. However, PLUS-RNN is cited by two papers which train pLMs which take in multi-peptide inputs: ProteinGLUE multi-task benchmark suite for self-supervised protein modeling [4], and A novel antibacterial peptide recognition algorithm based on BERT [5].

Therefore, the final set of papers includes: Pre-Training of Deep Bidirectional Protein Sequence Representations With Structural Information, NABP-BERT: NANOBODY®️-antigen binding prediction based on bidirectional encoder representations from transformers (BERT) architecture, PLM-interact: extending protein language models to predict protein-protein interactions, ProteinGLUE multi-task benchmark suite for self-supervised protein modeling, and A novel antibacterial peptide recognition algorithm based on BERT.

Extracting relevant information
For the five papers, the titles and all the relationships used to represent 'next sentences' between two proteins and their categories are as follows:

Paper title: Pre-Training of Deep Bidirectional Protein Sequence Representations with Structural Information. [1] (1 NSP-like relationship only)

The PLUS-RNN paper uses same-family prediction (SFP) to learn global structural information, citing the original BERT paper as motivation when developing their protein-specific pre-training task. In the paper, Pfam annotations [6] were collected for over 14 million proteins from 3,150 different families. If the two proteins in the input were both samples from the same Pfam family, they were considered to be 'next sentences', and were randomly sampled otherwise. (Since Pfam annotations are constructed via sequence alignment models, this relationship is considered to be evolutionary).
Paper title: NABP-BERT: NANOBODY®️-antigen binding prediction based on bidirectional encoder representations from transformers (BERT) architecture [2] (3 NSP-like relationships used at different training stages)

In the first training stage outlined in the three part NABP-BERT model training scheme, the PROT-BERT model is trained to learn fundamental protein semantics. At this point, the model is trained to predict if the if the following protein sequence is 'next' in the documents constructed from the UniProt database. In practice, this means that during training, two proteins are considered 'next sentences' if they are adjacent in the training set. Otherwise, they are considered to not be 'next sentences'. (This relationship does not depend on physical protein characteristics, or the proteins evolutionary similarities, so it belongs in the other category).
During the second stage of model training (and the first stage of supervised finetuning) the PPI-PROT-BERT model is finetuned from the PROT-BERT model to predict protein-protein interactions. At this point, the previous NSP-like output is fine-tuned to predict interreacting or not-interacting labels for the input protein pairs, as collected from the HINT database [7]. (Since this relationship is based on if the two proteins in the input pair participate in a protein protein interaction, it is considered to be physical.)
During the third stage of model training (and the second stage of supervised finetuning) the PPI-PROT-BERT model was finetuned to create the final NABP-PPI-PROT-BERT model to predict the binding between NANOBODY®️ (NB) and antigen (Ag) sequences. The NSP-like objective used at this point was changed from PPI interaction label prediction to predicting if the NB and Ag peptide sequences in the input pair are an interacting pair, or not. (Since this relationship is based on if the input pair NB protein binds the Ag protein, it is considered to be physical.)
Paper title: PLM-interact: extending protein language models to predict protein-protein interactions [3] (1 NSP-like relationship only)

The PLM-Interact model implements an explicitly "next sentence" inspired prediction task to fine tune the layers of an ESM-2 model to predict a binary label indicating if the input pair proteins interact or not. (Since this relationship is based on protein protein interactions, it is classified as physical).
Paper title: ProteinGLUE multi-task benchmark suite for self-supervised protein modeling [4] (1 NSP-like relationship only)

The NSP task was adapted for protein data by using a whole protein sequence with a SEP token inserted randomly (at a location 40-60% of the total sequence length) or by concatenating the first part of a protein with the second part of a different protein sequence separated by a SEP token. In this case, the whole protein case was considered to be a positive 'next sentence' relationship, while the randomly concatenated protein chunks case was considered to be a non-next sentence relationship. (Since this relationship is not based on the two input peptides acting on each other, or based on a specific evolutionary relationship, it is considered to be other).
Paper title: A novel antibacterial peptide recognition algorithm based on BERT [5] (1 NSP-like relationship only)

In the pre-training stage, the antibacterial peptide prediction model is trained on UniProt data to learn general protein semantics. In practice, this means that during training, two proteins are considered 'next sentences' if they are adjacent in the training set documents extracted from UniProt. Otherwise, they are considered to not be 'next sentences'. (This relationship does not depend on physical protein characteristics, or the proteins evolutionary similarities, so it belongs in the other category).

Relationship category pie chart
There are seven NSP-like relationships in the five papers: one evolutionary, three physical, and three other. This corresponds to 14.29% for the evolutionary category, 42.86% for the physical category, and 42.86% for the other category.

Pie chart description: The pie chart is titled 'Types of NSP-like relationships' and has three slices. If treating the pie chart like a clock, there is a blue slice that extends from around 10 o'clock to 12 o'clock. It has the text '14.29%' centered in the slice, and the label 'evolutionary' appears next to the slice. There is a gray slice from approximately 5 o'clock to 10 o'clock. The gray slice has the text '42.86%' centered in it, and the label 'other' appears next to the slice. Finally, the last slice completing the pie chart is red, and goes from about 12 o'clock to about 5 o'clock It has the text '42.86%' centered in it, and the label 'physical' appears next to it.

References:

1. Min, S. et al. Pre-training of deep bidirectional protein sequence representations with structural information. IEEE Access 9, 123912–123926 (2021). https://doi.org/10.1109/ACCESS.2021.3110269

2. Ahmed, F. S., Aly, S. & Liu, X. NABP-BERT: nanobody–antigen binding prediction based on bidirectional encoder representations from transformers architecture. Brief. Bioinform. 26, bbae518 (2025). https://doi.org/10.1093/bib/bbae518

3. Liu, D. et al. PLM-interact: extending protein language models to predict protein–protein interactions. Nat. Commun. 16, 9012 (2025). https://doi.org/10.1038/s41467-025-64512-w

4. Capel, H. et al. ProteinGLUE multi-task benchmark suite for self-supervised protein modeling. Sci. Rep. 12, 16047 (2022). https://doi.org/10.1038/s41598-022-19608-4

5. Zhang, Y., Lin, J., Zhao, L., Zeng, X. & Liu, X. A novel antibacterial peptide recognition algorithm based on BERT. Brief. Bioinform. 22, bbab200 (2021). https://doi.org/10.1093/bib/bbab200

6. Finn, R. D. et al. Pfam: the protein families database. Nucleic Acids Res. 42, D222–D230 (2014). https://doi.org/10.1093/nar/gkt1223

7. Das, J. & Yu, H. HINT: high-quality protein interactomes and their applications in understanding human disease. BMC Syst. Biol. 6, 92 (2012). https://doi.org/10.1186/1752-0509-6-92
