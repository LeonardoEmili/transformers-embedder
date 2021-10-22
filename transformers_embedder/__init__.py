from transformers_embedder import utils

if utils.is_torch_available():
    from transformers_embedder.embedder import TransformersEmbedder

from transformers_embedder.tokenizer import Tokenizer

from transformers import (
    BertTokenizer,
    BertTokenizerFast,
    BertweetTokenizer,
    CamembertTokenizer,
    CamembertTokenizerFast,
    DebertaTokenizer,
    DistilBertTokenizer,
    DistilBertTokenizerFast,
    MobileBertTokenizer,
    MobileBertTokenizerFast,
    RobertaTokenizer,
    RobertaTokenizerFast,
    XLMRobertaTokenizer,
    XLMRobertaTokenizerFast,
    XLMTokenizer,
)


MODELS_WITH_STARTING_TOKEN = (
    BertTokenizer,
    BertTokenizerFast,
    DistilBertTokenizer,
    DistilBertTokenizerFast,
    MobileBertTokenizer,
    MobileBertTokenizerFast,
    BertweetTokenizer,
    CamembertTokenizer,
    CamembertTokenizerFast,
    DebertaTokenizer,
    RobertaTokenizer,
    RobertaTokenizerFast,
    XLMRobertaTokenizer,
    XLMRobertaTokenizerFast,
    XLMTokenizer,
)

MODELS_WITH_DOUBLE_SEP = (
    CamembertTokenizer,
    CamembertTokenizerFast,
    BertweetTokenizer,
    RobertaTokenizer,
    RobertaTokenizerFast,
    XLMRobertaTokenizer,
    XLMRobertaTokenizerFast,
)