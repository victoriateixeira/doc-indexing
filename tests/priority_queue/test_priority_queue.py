from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    regular_priority = {
        "nome_do_arquivo": "arquivo_teste1.txt",
        "qtd_linhas": 6,
        "linhas_do_arquivo": [],
    }
    high_priority_1 = {
        "nome_do_arquivo": "arquivo_teste2.txt",
        "qtd_linhas": 3,
        "linhas_do_arquivo": [],
    }
    high_priority_2 = {
        "nome_do_arquivo": "arquivo_teste3.txt",
        "qtd_linhas": 4,
        "linhas_do_arquivo": [],
    }

    priority_queue.enqueue(regular_priority)
    priority_queue.enqueue(high_priority_1)
    priority_queue.enqueue(high_priority_2)
    assert len(priority_queue.regular_priority) == 1
    assert len(priority_queue.high_priority) == 2

    first_out = priority_queue.dequeue()
    assert len(priority_queue.high_priority) == 1
    assert len(priority_queue.regular_priority) == 1
    assert first_out == high_priority_1

    assert priority_queue.search(0) == high_priority_2
    assert priority_queue.search(1) == regular_priority

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(50)
