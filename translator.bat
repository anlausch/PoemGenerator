python generator.py
python sp_encoder.py C:/Users/anlausch/workspace/gedichter/en-poem.txt C:/Users/anlausch/workspace/gedichter/en-poem.txt.sp
python C:/Users/anlausch/workspace/gedichter/OpenNMT-py-master/translate.py -model C:/Users/anlausch/workspace/gedichter/model_en_de/averaged-10-epoch.pt -src C:/Users/anlausch/workspace/gedichter/en-poem.txt.sp -output C:/Users/anlausch/workspace/gedichter/de-poem.txt.sp
python sp_decoder.py C:/Users/anlausch/workspace/gedichter/de-poem.txt.sp C:/Users/anlausch/workspace/gedichter/de-poem.txt
