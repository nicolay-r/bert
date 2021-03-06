import os
import random

import tokenization
import tensorflow as tf
from core.data_processor import DataProcessor
from core.input_example import InputExample


flags = tf.flags
FLAGS = flags.FLAGS

filename_template = "sample-{data_type}-{cv_index}.tsv.gz"

# Mix of the origininal data, as the latter in case of 'train' type
# mostly represents a sequence of a zero labeled examples.
RANDOM_SEED = 1


class SAE_2SM_Processor(DataProcessor):
    """Processor for the SAE data set, three scale classification format
       SAE stands for "Sentiment Attitude Extraction
       2 -- Three scale
       S -- Single sentence (text_a only)
       M -- multiple classification
       Columns:
            test: [id, text_a]
            train: [id, label, text_a]
    """

    def get_train_examples(self, data_dir):
        """See base class."""
        filename = filename_template.format(data_type='train', cv_index=FLAGS.cv_index)
        return self._create_examples(self._read_tsv_gzip(os.path.join(data_dir, filename)), "train")

    def get_dev_examples(self, data_dir):
        return self.get_train_examples(data_dir)

    def get_test_examples(self, data_dir):
        """See base class."""
        filename = filename_template.format(data_type='test', cv_index=FLAGS.cv_index)
        return self._create_examples(
            self._read_tsv_gzip(os.path.join(data_dir, filename)), "test")

    def get_labels(self):
        """See base class."""
        return ["0", "1"]

    def _create_examples(self, lines, set_type):
        """Creates examples for the training and dev sets."""
        examples = []
        for (i, line) in enumerate(lines):
            # Only the test set has a header
            if i == 0:
                continue
            guid = "%s-%s" % (set_type, i)
            if set_type == "test":
                # Headers: id, news_id, text_a, s_obj, t_obj
                label = "0"
                text_a = tokenization.convert_to_unicode(line[2])
                s_obj = tokenization.convert_to_unicode(line[3])
                t_obj = tokenization.convert_to_unicode(line[4])
            else:
                # Headers: id, news_id, label, text_a, s_obj, t_obj
                label = tokenization.convert_to_unicode(line[2])
                text_a = tokenization.convert_to_unicode(line[3])
                s_obj = tokenization.convert_to_unicode(line[4])
                t_obj = tokenization.convert_to_unicode(line[5])

            examples.append(
                InputExample(guid=guid,
                             text_a=text_a,
                             text_b=None,
                             s_obj=int(s_obj),
                             t_obj=int(t_obj),
                             label=label))

        if set_type == "train":
            random.Random(RANDOM_SEED).shuffle(examples)

        return examples


class SAE_3SM_Processor(SAE_2SM_Processor):

    def get_labels(self):
        """See base class."""
        return ["0", "1", "2"]


class SAE_PB_Processor(DataProcessor):
    """Processor for the SAE data set, three scale classification format
       SAE stands for "Sentiment Attitude Extraction
       P -- Pair of sentences (text_a, text_b)
       B -- Binary classification
       Columns:
            test: [id, text_a, text_b]
            train: [id, label, text_a, text_b]
    """

    def get_train_examples(self, data_dir):
        """See base class."""
        filename = filename_template.format(data_type='train', cv_index=FLAGS.cv_index)
        return self._create_examples(
            self._read_tsv_gzip(os.path.join(data_dir, filename)), "train")

    def get_dev_examples(self, data_dir):
        return self.get_train_examples(data_dir)

    def get_test_examples(self, data_dir):
        """See base class."""
        filename = filename_template.format(data_type='test', cv_index=FLAGS.cv_index)
        return self._create_examples(
            self._read_tsv_gzip(os.path.join(data_dir, filename)), "test")

    def get_labels(self):
        """See base class."""
        return ["0", "1"]

    def _create_examples(self, lines, set_type):
        """Creates examples for the training and dev sets."""
        examples = []
        for (i, line) in enumerate(lines):
            # Only the test set has a header
            if i == 0:
                continue
            guid = "%s-%s" % (set_type, i)
            if set_type == "test":
                # Headers: id, news_id, text_a, text_b, s_obj, t_obj
                label = "0"
                text_a = tokenization.convert_to_unicode(line[2])
                text_b = tokenization.convert_to_unicode(line[3])
                s_obj = tokenization.convert_to_unicode(line[4])
                t_obj = tokenization.convert_to_unicode(line[5])
            else:
                # Headers: id, news_id, label, text_a, text_b, s_obj, t_obj
                label = tokenization.convert_to_unicode(line[2])
                text_a = tokenization.convert_to_unicode(line[3])
                text_b = tokenization.convert_to_unicode(line[4])
                s_obj = tokenization.convert_to_unicode(line[5])
                t_obj = tokenization.convert_to_unicode(line[6])

            examples.append(
                InputExample(guid=guid,
                             text_a=text_a,
                             text_b=text_b,
                             s_obj=int(s_obj),
                             t_obj=int(t_obj),
                             label=label))

        if set_type == "train":
            random.Random(RANDOM_SEED).shuffle(examples)

        return examples


class SAE_2PM_Processor(DataProcessor):
    """Processor for the SAE data set, three scale classification format
       SAE stands for "Sentiment Attitude Extraction
       2 -- Three scale
       P -- Pair of sentences (text_a, text_b)
       M -- Multiple classification
       Columns:
            test: [id, text_a, text_b]
            train: [id, label, text_a, text_b]
    """

    def get_train_examples(self, data_dir):
        """See base class."""
        filename = filename_template.format(data_type='train', cv_index=FLAGS.cv_index)
        return self._create_examples(
            self._read_tsv_gzip(os.path.join(data_dir, filename)), "train")

    def get_dev_examples(self, data_dir):
        return self.get_train_examples(data_dir)

    def get_test_examples(self, data_dir):
        """See base class."""
        filename = filename_template.format(data_type='test', cv_index=FLAGS.cv_index)
        return self._create_examples(
            self._read_tsv_gzip(os.path.join(data_dir, filename)), "test")

    def get_labels(self):
        """See base class."""
        return ["0", "1"]

    def _create_examples(self, lines, set_type):
        """Creates examples for the training and dev sets."""
        examples = []
        for (i, line) in enumerate(lines):
            # Only the test set has a header
            if i == 0:
                continue
            guid = "%s-%s" % (set_type, i)
            if set_type == "test":
                # Headers: id, news_id, text_a, text_b, s_obj, t_obj
                label = "0"
                text_a = tokenization.convert_to_unicode(line[2])
                text_b = tokenization.convert_to_unicode(line[3])
                s_obj = tokenization.convert_to_unicode(line[4])
                t_obj = tokenization.convert_to_unicode(line[5])
            else:
                # Headers: id, news_id, label, text_a, text_b, s_obj, t_obj
                label = tokenization.convert_to_unicode(line[2])
                text_a = tokenization.convert_to_unicode(line[3])
                text_b = tokenization.convert_to_unicode(line[4])
                s_obj = tokenization.convert_to_unicode(line[5])
                t_obj = tokenization.convert_to_unicode(line[6])

            examples.append(
                InputExample(guid=guid,
                             text_a=text_a,
                             text_b=text_b,
                             s_obj=int(s_obj),
                             t_obj=int(t_obj),
                             label=label))

        if set_type == "train":
            random.Random(RANDOM_SEED).shuffle(examples)

        return examples


class SAE_3PM_Processor(SAE_2PM_Processor):

    def get_labels(self):
        """See base class."""
        return ["0", "1", "2"]
