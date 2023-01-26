import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("falha", "falha")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(65, 65)

    assert encrypt_message("teste1", 3) == "set_1et"
    assert encrypt_message("teste2", 3) == "set_2et"
    assert encrypt_message("teste3", 7) == "3etset"
