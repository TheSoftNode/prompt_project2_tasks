Golden response

Analysis of martiansideofthemoon/ai-detection-paraphrases GitHub repository
Introduction
The paper associated with the martiansideofthemoon/ai-detection-paraphrases GitHub repository is titled “Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense” [1]. Its first author is Kalpesh Krishna. In this paper, one of the generator models tested is called text-davinci-003. This generator originates from the seminal GPT-3 paper, “Language Models are Few-Shot Learners” [2]. This paper’s first author is Tom Brown. The paraphrasing model used in the repository’s paper is a sequence-to-sequence transformer. The transformer architecture originates from the seminal paper “Attention Is All You Need. [3]. This paper’s first author is Ashish Vaswani.

Transformer Comparison
The transformer used in “Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense” to paraphrase text samples and evade detection is a significant evolution from the original transformer concept and architecture. The exact architecture used for paraphrasing originates from “Exploring the limits of transfer learning with a unified text-to-text transformer” [4] by Colin Rafell et al., published in 2019. Below is a comparison of the two transformers on several architecture details and evaluation metrics.

Transformer (big)

    Parameters (millions) - 213

    d_model - 1024

    d_ff - 4096

    Attention Heads - 16

    BLEU (EN-DE) - 28.4

    BLEU (EN-FR) - 41.8

T5-11B

    Parameters (millions) - 11000

    d_model - 1024

    d_ff - 65536

    Attention Heads - 128

    BLEU (EN-DE) - 32.1

    BLEU (EN-FR) - 43.4

Parameter Count Chart
Below is a graph comparing the parameter count of the three generator models and one paraphrasing model used in “Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense. OPT-13B comes from "OPT: Open Pre-trained Transformer Language Models" [5].

Description: The chart is a simple bar chart titled “Model Parameter Comparison.” The y-axis is labeled “Parameters (millions)” and its values range from 1 to 1000000. The x-axis is labeled “Model” and has four items: GPT2-XL, OPT-13B, text-davinci-003, and T5-XXL. The first three of these are colored red, and the final one (T5-XXL) is colored blue. The GPT2-XL bar extends to 1500 (just above the 1000 line). The OPT-13B bar extends to 13000 (just above the 10000 line). The text-davinci-003 bar extends to 175000 (just above the 100000 line). The T5-XXL bar extends to 11000 (just above the 10000 line, but lower than OPT-13B).

Paraphrasing Script
In the martiansideofthemoon/ai-detection-paraphrases GitHub repository, the script that uses the Dipper model to paraphrase text is dipper_paraphrases/paraphrase.py. The command line arguments defined in the script are as follows:

–output_file: Points to the file in which the outputted phrases should be stored.

–model: Identifies the model architecture to be used for paraphrasing.

–num_shards: Number of partitions to split the data with.

–local_rank: Which partition to use for this run.

–sent_interval: This number of sentences will be grouped in each paraphrasing window

Citations
[1] Krishna, K., Song, Y., Karpinska, M., Wieting, J., & Iyyer, M. (2023). Paraphrasing evades detectors of AI-generated text, but retrieval is an effective defense. arXiv [Cs.CL]. Retrieved from http://arxiv.org/abs/2303.13408

[2] Brown, T. B., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., … Amodei, D. (2020). Language Models are Few-Shot Learners. arXiv [Cs.CL]. Retrieved from http://arxiv.org/abs/2005.14165

[3] Vaswani, A., Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A. N., … Polosukhin, I. (2023). Attention Is All You Need. arXiv [Cs.CL]. Retrieved from http://arxiv.org/abs/1706.03762

[4] Raffel, C., Shazeer, N., Roberts, A., Lee, K., Narang, S., Matena, M., … Liu, P. J. (2023). Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer. arXiv [Cs.LG]. Retrieved from http://arxiv.org/abs/1910.10683

[5] Zhang, S., Roller, S., Goyal, N., Artetxe, M., Chen, M., Chen, S., … Zettlemoyer, L. (2022). OPT: Open Pre-trained Transformer Language Models. arXiv [Cs.CL]. Retrieved from http://arxiv.org/abs/2205.01068
