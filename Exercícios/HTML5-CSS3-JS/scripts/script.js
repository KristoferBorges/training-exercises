let jogador = {
    nome: "KiroGaia",
    classe: "Guerreiro",
    caracteristicas: {
        vida: 100,
        forca: 15,
        defesa: 20,
        velocidade: 5,
        stamina: 20,
        status: "Vivo"
    },
    equipamentos: {
        arma: {
            nome: "Espada",
            dano: 10     
        },
        capacete: {
            nome: "Vazio",
            defesa: 0
        },
        peitoral: {
            nome: "Peitoral de Ferro",
            defesa: 10
        },
        botas: {
            nome: "Botas de Couro",
            defesa: 2,
            velocidade: 1
        },
    },
};

let monstros = [
    {
        nome: "Globin",
        class: "Nenhuma",
        tipo: "Terrestre",
        caracteristicas: {
            vida: 60,
            forca: 21,
            defesa: 2,
            velocidade: 6,
            stamina: 10,
            status: "Vivo"
        }
    },
    {
        nome: "Dragão",
            class: "Chefe",
            tipo: "Voador",
            caracteristicas: {
                vida: 300,
                forca: 50,
                defesa: 20,
                velocidade: 10,
                stamina: 50,
                status: "Vivo"
        }
    },
    {
        nome: "Esqueleto",
        class: "Nenhuma",
        tipo: "Terrestre",
        caracteristicas: {
            vida: 40,
            forca: 10,
            defesa: 5,
            velocidade: 4,
            stamina: 5,
            status: "Vivo"
    },
}];

function addAtributeJogador(obj) {

    if (obj.arma.nome == "Vazio") {
        console.log("Arma não equipada!");
    } else {
        console.log(`${obj.arma.nome} equipada! + ${obj.arma.dano} de dano.`);
        jogador.caracteristicas.forca += obj.arma.dano;
    };

    if (obj.capacete.nome == "Vazio") {
        console.log("Capacete não equipado!");
    } else {
        console.log(`${obj.capacete.nome} equipado! + ${obj.capacete.defesa} de defesa.`);
        jogador.caracteristicas.defesa += obj.capacete.defesa;
    };

    if (obj.peitoral.nome == "Vazio") {
        console.log("Peitoral não equipado!");
    } else {
        console.log(`${obj.peitoral.nome} equipado! + ${obj.peitoral.defesa} de defesa.`);
        jogador.caracteristicas.defesa += obj.peitoral.defesa;
    };

    if (obj.botas.nome == "Vazio") {
        console.log("Botas não equipadas!");
    } else {
        console.log(`${obj.botas.nome} equipadas! + ${obj.botas.defesa} de defesa e + ${obj.botas.velocidade} de velocidade.`);
        jogador.caracteristicas.defesa += obj.botas.defesa;
        jogador.caracteristicas.velocidade += obj.botas.velocidade;
    };
    console.log(jogador.caracteristicas);
    console.log(monstros[0].caracteristicas);
};

function addAtributeMob(obj) {

    if (obj.arma.nome == "Vazio") {
        console.log("Arma não equipada!");
    } else {
        console.log(`${obj.arma.nome} equipada! + ${obj.arma.dano} de dano.`);
        jogador.caracteristicas.forca += obj.arma.dano;
    };

    if (obj.capacete.nome == "Vazio") {
        console.log("Capacete não equipado!");
    } else {
        console.log(`${obj.capacete.nome} equipado! + ${obj.capacete.defesa} de defesa.`);
        jogador.caracteristicas.defesa += obj.capacete.defesa;
    };

    if (obj.peitoral.nome == "Vazio") {
        console.log("Peitoral não equipado!");
    } else {
        console.log(`${obj.peitoral.nome} equipado! + ${obj.peitoral.defesa} de defesa.`);
        jogador.caracteristicas.defesa += obj.peitoral.defesa;
    };

    if (obj.botas.nome == "Vazio") {
        console.log("Botas não equipadas!");
    } else {
        console.log(`${obj.botas.nome} equipadas! + ${obj.botas.defesa} de defesa e + ${obj.botas.velocidade} de velocidade.`);
        jogador.caracteristicas.defesa += obj.botas.defesa;
        jogador.caracteristicas.velocidade += obj.botas.velocidade;
    };
};

function attack(atacante, defensor) {
    // Definição do quanto de dano será causado
    let dano = atacante.caracteristicas.forca - defensor.caracteristicas.defesa;

    // Verificação de valores negativos & Redução de status
    if (dano < 0) {
        dano = 0;
    };
    defensor.caracteristicas.vida -= dano;

    if (defensor.caracteristicas.vida < 0) {
        defensor.caracteristicas.vida = 0;
    };
    defensor.caracteristicas.defesa -= atacante.caracteristicas.forca * 0.2;

    if (atacante.caracteristicas.velocidade < 0) {
        atacante.caracteristicas.velocidade = 0;
    };
    atacante.caracteristicas.velocidade -= atacante.caracteristicas.stamina * 0.5;

    // Verificação dos status menores que 0
    if (defensor.caracteristicas.vida < 0) {
        defensor.caracteristicas.vida = 0;
    };
    if (defensor.caracteristicas.defesa < 0) {
        defensor.caracteristicas.defesa = 0;
    };
    if (atacante.caracteristicas.velocidade < 0) {
        atacante.caracteristicas.velocidade = 0;
    };
    
    console.log(`${atacante.nome} atacou ${defensor.nome} e causou ${dano.toFixed(2)} de dano.`);

    if (defensor.caracteristicas.vida <= 0) {
        defensor.caracteristicas.status = "Morto";
        console.log(`${defensor.nome} morreu.`);
    };
};

function fight(player_1, mob) {
    addAtributeJogador(player_1.equipamentos);
    //addAtributeMob(mob.equipamentos);

    while (player_1.caracteristicas.status == "Vivo" && mob.caracteristicas.status == "Vivo") {
        if (player_1.caracteristicas.velocidade > mob.caracteristicas.velocidade) {
            attack(atacante=player_1, defensor=mob);
        } else if (player_1.caracteristicas.velocidade < mob.caracteristicas.velocidade) {
            attack(atacante=mob, defensor=player_1);
        } else {
            console.log("Velocidade equiparada, ataques simultâneos!!!");
            attack(atacante=player_1, defensor=mob);
            attack(atacante=mob, defensor=player_1);
        };

        if (false){
            //Descrição das características dos jogadores após a luta
            console.log(`JOGADOR ${player_1.nome}`)
            console.log(`Vida: ${player_1.caracteristicas.vida}`);
            console.log(`Força: ${player_1.caracteristicas.forca}`);
            console.log(`Defesa: ${player_1.caracteristicas.defesa}`);
            console.log(`Velocidade: ${player_1.caracteristicas.velocidade}`);
            console.log(`Stamina: ${player_1.caracteristicas.stamina}`);
            console.log(`Status: ${player_1.caracteristicas.status}`);

            console.log(`MONSTRO ${mob.nome}`)
            console.log(`Vida: ${mob.caracteristicas.vida}`);
            console.log(`Força: ${mob.caracteristicas.forca}`);
            console.log(`Defesa: ${mob.caracteristicas.defesa}`);
            console.log(`Velocidade: ${mob.caracteristicas.velocidade}`);
            console.log(`Stamina: ${mob.caracteristicas.stamina}`);
            console.log(`Status: ${mob.caracteristicas.status}`);
        };
    };
};

// Criar cópias profundas dos objetos
let copiaPlayer = structuredClone(jogador);
let copiaMob = structuredClone(monstros[0]);

//fight(copiaPlayer, copiaMob);