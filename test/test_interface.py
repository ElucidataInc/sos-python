#!/usr/bin/env python3
#
# Copyright (c) Bo Peng and the University of Texas MD Anderson Cancer Center
# Distributed under the terms of the 3-clause BSD License.

import os
import tempfile
import pytest
from sos_notebook.test_utils import NotebookTest


class TestInterface(NotebookTest):

    #
    # Python 2
    #
    def test_py2_prompt_color(self, notebook):
        '''test color of input and output prompt'''
        idx = notebook.call(
            '''\
            print('this is Python 2')
            ''',
            kernel="Python2")
        assert [255, 241, 119] == notebook.get_input_backgroundColor(idx)
        assert [255, 241, 119] == notebook.get_output_backgroundColor(idx)

    def test_py2_cd(self, notebook):
        '''Support for change of directory with magic %cd'''
        output1 = notebook.check_output(
            '''\
            import os
            print(os.getcwd())
            ''',
            kernel="Python2")
        notebook.call('%cd ..', kernel="SoS")
        output2 = notebook.check_output(
            '''\
            import os
            print(os.getcwd())
            ''',
            kernel="Python2")
        assert len(output1) > len(output2)
        assert output1.startswith(output2)
        #
        # cd to a specific directory
        tmpdir = os.path.join(tempfile.gettempdir(), 'somedir')
        os.makedirs(tmpdir, exist_ok=True)
        notebook.call(f'%cd {tmpdir}', kernel="SoS")
        output = notebook.check_output(
            '''\
            import os
            print(os.getcwd())
            ''',
            kernel="Python2")
        assert os.path.realpath(tmpdir) == os.path.realpath(output)

    def test_py2_auto_vars(self, notebook):
        '''Test automatic exchange of variables with names starting with sos'''
        notebook.call('sosInSoS = 123', kernel="SoS")
        assert '123' == notebook.check_output('sosInSoS', kernel='Python2')

        notebook.call('sosInPython2 = 12345', kernel="Python2")
        assert '12345' == notebook.check_output('sosInPython2', kernel='SoS')

    @pytest.mark.skip
    def test_py2_preview(self, notebook):
        '''Test support for %preview'''
        output = notebook.check_output(
            '''\
            %preview -n var
            var = seq(1, 1000)
            ''',
            kernel="Python2")
        # in a normal var output, 100 would be printed. The preview version would show
        # type and some of the items in the format of
        #   int [1:1000] 1 2 3 4 5 6 7 8 9 10 ...
        assert 'int' in output and '3' in output and '9' in output and '111' not in output
        #
        # return 'Unknown variable' for unknown variable
        assert 'Unknown variable' in notebook.check_output(
            '%preview -n unknown_var', kernel="Python2")
        #
        # return 'Unknown variable for expression
        assert 'Unknown variable' in notebook.check_output(
            '%preview -n var[1]', kernel="Python2")

    def test_py2_sessioninfo(self, notebook):
        '''test support for %sessioninfo'''
        notebook.call("print('this is Python2')", kernel="Python2")
        assert 'Python2' in notebook.check_output('%sessioninfo', kernel="SoS")

    #
    # Python 3
    #
    def test_py3_prompt_color(self, notebook):
        '''test color of input and output prompt'''
        idx = notebook.call(
            '''\
            print('this is Python 3')
            ''',
            kernel="Python3")
        assert [255, 217, 26] == notebook.get_input_backgroundColor(idx)
        assert [255, 217, 26] == notebook.get_output_backgroundColor(idx)

    def test_py3_cd(self, notebook):
        '''Support for change of directory with magic %cd'''
        output1 = notebook.check_output(
            '''\
            import os
            print(os.getcwd())
            ''',
            kernel="Python3")
        notebook.call('%cd ..', kernel="SoS")
        output2 = notebook.check_output(
            '''\
            import os
            print(os.getcwd())
            ''',
            kernel="Python3")
        assert len(output1) > len(output2)
        assert output1.startswith(output2)
        #
        # cd to a specific directory
        tmpdir = os.path.join(tempfile.gettempdir(), 'somedir')
        os.makedirs(tmpdir, exist_ok=True)
        notebook.call(f'%cd {tmpdir}', kernel="SoS")
        output = notebook.check_output(
            '''\
            import os
            print(os.getcwd())
            ''',
            kernel="Python3")
        assert os.path.realpath(tmpdir) == os.path.realpath(output)

    def test_py3_auto_vars(self, notebook):
        '''Test automatic exchange of variables with names starting with sos'''
        notebook.call('sosInSoS = 123', kernel="SoS")
        assert '123' == notebook.check_output('sosInSoS', kernel='Python3')

        notebook.call('sosInPython3 = 12345', kernel="Python3")
        assert '12345' == notebook.check_output('sosInPython3', kernel='SoS')

    @pytest.mark.skip
    def test_py3_preview(self, notebook):
        '''Test support for %preview'''
        output = notebook.check_output(
            '''\
            %preview -n var
            var = seq(1, 1000)
            ''',
            kernel="Python3")
        # in a normal var output, 100 would be printed. The preview version would show
        # type and some of the items in the format of
        #   int [1:1000] 1 2 3 4 5 6 7 8 9 10 ...
        assert 'int' in output and '3' in output and '9' in output and '111' not in output
        #
        # return 'Unknown variable' for unknown variable
        assert 'Unknown variable' in notebook.check_output(
            '%preview -n unknown_var', kernel="Python3")
        #
        # return 'Unknown variable for expression
        assert 'Unknown variable' in notebook.check_output(
            '%preview -n var[1]', kernel="Python3")

    def test_py3_sessioninfo(self, notebook):
        '''test support for %sessioninfo'''
        notebook.call("print('this is Python3')", kernel="Python3")
        assert 'Python3' in notebook.check_output('%sessioninfo', kernel="SoS")
