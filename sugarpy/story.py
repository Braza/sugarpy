import xml.etree.ElementTree
from antlr4 import *
from sugarpy.SugarCubeLexer import SugarCubeLexer
from sugarpy.SugarCubeParser import SugarCubeParser
from sugarpy.SugarCubeVisitor import SugarCubeVisitor


class Story:

    def __init__(self, story_data, story_vars):
        """

            Args:
                story_data (str): Description of `param1`.
                story_vars (dict): Initial story variables.

        """
        self.story_root = xml.etree.ElementTree.fromstring(story_data)
        self.story_vars = story_vars



    def get_raw_scene(self, scene_name=None):
        """Return the raw text of the story scene.

        Args:
            scene_name (str): Name of the scene to return. If not supplied, then the story start scene is returned.

        Returns:
            str: Raw scene text including SugarCube markup.

        Todo:
        * Add error handling for not found scene name
        """
        if scene_name:
            scene = self.story_root.find("./tw-passagedata[@name='{}']".format(scene_name))
        else:
            start_scene_id = self.story_root.attrib['startnode']
            scene = self.story_root.find("./tw-passagedata[@pid='{}']".format(start_scene_id))

        if scene is not None:
            return scene.text

    def get_processed_scene(self, scene_name=None):
        text = self.get_raw_scene(scene_name)
        input_stream = InputStream(text)
        lexer = SugarCubeLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = SugarCubeParser(stream)
        visitor = SugarCubeVisitor(self.story_vars)
        rendered_text = visitor.visit(parser.parse())
        return rendered_text

    def get_rendered_scene(self, renderer, scene_name=None):
        return renderer(self.get_processed_scene(scene_name))
