class InputExample(object):
  """A single training/test example for simple sequence classification."""

  ESource = '#ES'
  ETarget = '#ET'

  def __init__(self, guid, text_a, s_obj, t_obj, text_b=None, label=None):
    """Constructs a InputExample.

    Args:
      guid: Unique id for the example.
      text_a: string. The untokenized text of the first sequence. For single
        sequence tasks, only this sequence must be specified.
      text_b: (Optional) string. The untokenized text of the second sequence.
        Only must be specified for sequence pair tasks.
      label: (Optional) string. The label of the example. This should be
        specified for train and dev examples, but not for test examples.
    """
    self.guid = guid
    self.text_a = self.__replace_ends(text_a, s_obj, t_obj)
    self.text_b = text_b
    self.label = label

  @staticmethod
  def __replace_ends(data, s_obj, t_obj):
    """ Replacing ends in order to find them later, after tokenization
    """
    data[s_obj] = InputExample.ESource
    data[t_obj] = InputExample.ETarget
