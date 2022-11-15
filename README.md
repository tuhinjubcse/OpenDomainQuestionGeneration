# OpenDomainQuestionGeneration

Code and data for EMNLP 2022 paper "CONSISTENT: Open-Ended Question Generation From News Articles"

          The model trained on ELI5 with control code can be found herehttps://huggingface.co/TuhinColumbia/QAGenControlCode

          To run inference you can put ControlCode +' ====== '+ Paragraph


          The allparagraph.json file contains generated question from all baselines while amtwittenquestions.csv contain gold answers

          You can also find the article metadata along with QA model confidence scores in respective domain folders for generated questions 


If you use our code, data or model please cite us

                      @article{chakrabarty2022consistent,
                        title={CONSISTENT: Open-Ended Question Generation From News Articles},
                        author={Chakrabarty, Tuhin and Lewis, Justin and Muresan, Smaranda},
                        journal={arXiv preprint arXiv:2210.11536},
                        year={2022}
                      }
