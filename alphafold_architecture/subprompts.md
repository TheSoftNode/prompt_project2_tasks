SUBPROMPTS

Sub-prompt #1: How many recycling iterations does AlphaFold use according to the Nature paper?
Sub-prompt #1 Answer: 3

Sub-prompt #2: How many Evoformer blocks does AlphaFold have?
Sub-prompt #2 Answer: 48

Sub-prompt #3: What is the d_model (msa_channel) for AlphaFold?
Sub-prompt #3 Answer: 256

Sub-prompt #4: What is the d_ff for AlphaFold?
Sub-prompt #4 Answer: 1024

Sub-prompt #5: How many encoder layers does Transformer (big) have?
Sub-prompt #5 Answer: 6

Sub-prompt #6: What is the d_model for Transformer (big)?
Sub-prompt #6 Answer: 1024

Sub-prompt #7: What is the d_ff for Transformer (big)?
Sub-prompt #7 Answer: 4096

Sub-prompt #8: What is the weights-only matrix-parameter count formula for one Transformer encoder layer?
Sub-prompt #8 Answer: 4 × d_model² + 2 × d_model × d_ff

Sub-prompt #9: What is the total weights-only Q/K/V/O plus FFN matrix parameter count for the Evoformer MSA path across 48 blocks?
Sub-prompt #9 Answer: 50,331,648

Sub-prompt #10: What is the Transformer (big) encoder stack weights-only matrix-parameter total?
Sub-prompt #10 Answer: 75,497,472

Sub-prompt #11: What is the effective sequential depth for AlphaFold?
Sub-prompt #11 Answer: 144

Sub-prompt #12: What is the parameter efficiency metric?
Sub-prompt #12 Answer: weights-only matrix parameters ÷ effective sequential depth

Sub-prompt #13: Which architecture achieves better parameter efficiency when accounting for depth?
Sub-prompt #13 Answer: AlphaFold
