const validarUsuario = (usuario, senha) => {
    if (usuario === 'Pedro' && senha === '123'){
        return alert('Usuário logado com sucesso!');
    } else {
        return alert('Usuário ou senha inválidos!');
    }
}

validarUsuario('Pedro', '1234');