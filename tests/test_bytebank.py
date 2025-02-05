from app.bytebank import Funcionario
import pytest

class TestClass:    
    def test_quando_idade_recebe_06_08_1997_deve_retornar_27(self):

        # Given - Contexto do teste
        entrada = "06/08/1997"
        esperado = 28

        funcionario_teste = Funcionario("teste", entrada,1111)

        # When - Ação do teste
        resultado = funcionario_teste.idade()

        #Then - Desfecho do teste
        assert resultado == esperado

    def test_quando_sobrenome_recebe_Teste_Santos_deve_retornar_Santos(self):
        
        # Given - Contexto do teste
        entrada = " Teste Santos "
        esperado = "Santos"

        funcionario_teste = Funcionario(entrada, "11/11/2000",1111)

        # When - Ação do teste
        resultado = funcionario_teste.sobrenome()

        #Then - Desfecho do teste
        assert resultado == esperado