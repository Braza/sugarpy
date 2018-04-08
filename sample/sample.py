from sugarpy.story import Story


fname = './sample.xml'
with open(fname, "r") as f:
    test_story_string = f.read()
    test_story = Story(test_story_string, {})
    print(test_story.get_raw_scene())
    print(test_story.get_processed_scene())
