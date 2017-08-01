from Menu import *
import pytest
import mock

class TestMain:

    def test_Menu_Empty_Input(self, capfd):
        with pytest.raises(SystemExit):
            with mock.patch('builtins.input', side_effect=
            ['', '', '6']):
                main()
        out, err = capfd.readouterr()
        assert "Error, select option 1-6" in out

    def test_Menu_Invalid_Input(self, capfd):
        with pytest.raises(SystemExit):
            with mock.patch('builtins.input', side_effect=
            ['a', '', '6']):
                main()
        out, err = capfd.readouterr()
        assert "Error, select option 1-6" in out