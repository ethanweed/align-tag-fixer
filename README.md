# align-tag-fixer

This project contains an alternate version of the ``prepare_transcripts`` module from the [ALIGN](https://github.com/nickduran/align-linguistic-alignment/tree/master) package. The motivation is to allow the user to add single custom phrases such as "a_little_bit" or "go_ahead" that the default Penn tagger would split into multiple words.

The ``tagfixer`` module relies on the user providing: 

1. a folder with Clan ``.cut`` files, containing the custom phrases, together with the corresponding chat-style tag. See the examples under samples/my-project/cut_files
2. a lookup table with a translation from chat to Penn format. An example is located in the ``res`` folder of this repository.

The module contains two functions:

1. ``chat2penn``, which creates a csv file with the custom phrases from the .cut files
2. ``prepare_transcripts``, which is exactly the same as the ALIGN function of the same the same name, but with the added feature of tagging the custom phrases with Penn-style tags.

See ``demo.ipynb`` in the samples folder for usage.

