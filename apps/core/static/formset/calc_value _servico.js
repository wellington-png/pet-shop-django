function calcularValor() {
    const input_quant = document.querySelectorAll('.quantidade');
    const input_valor = document.querySelectorAll('.valor');
    const input_servico = document.querySelectorAll('.servico');
    const input_valor_total = document.querySelectorAll('.valor_total');

    input_servico.forEach((servico, index) => {
        servico.addEventListener('change', () => {
            if (input_quant[index].value > 0) {
                $.ajax({
                    url: `http://127.0.0.1:8000/servico/get_value/${input_servico[index].value}/`,
                    type: "GET",
                    dataType: "json",
                    success: (data) => {
                        console.log(data.preco);
                        input_valor[index].value = data.preco;
                        input_valor_total[index].value = data.preco * input_quant[index].value;
                        valorTotalCompra()
                    },
                    error: (error) => {
                        console.log(error);
                    }
                });
            }
        })
    })

    input_quant.forEach((quant, index) => {
        quant.addEventListener('change', () => {
            const valor = quant.value;
            if (valor > 0) {
                $.ajax({
                    url: `http://127.0.0.1:8000/servico/get_value/${input_servico[index].value}/`,
                    type: "GET",
                    dataType: "json",
                    success: (data) => {
                        console.log(data.preco);
                        input_valor[index].value = data.preco;
                        input_valor_total[index].value = data.preco * valor;
                        valorTotalCompra();
                    },
                    error: (error) => {
                        console.log(error);
                    }
                });
            }

        })
    })

}

function valorTotalCompra() {
    const input_valor_total = document.querySelectorAll('.valor_total');
    const spam_valor_total = document.getElementById('valor_venda');
    soma = 0;

    input_valor_total.forEach((valor, index) => {
        soma += parseFloat(valor.value);
    });

    spam_valor_total.textContent = `R$ ${soma.toFixed(2)}`;
}


function changeTypeDate() {
    const input_data = document.getElementById('id_data_consulta');
    input_data.type = 'date';
    input_data.value = new Date().toISOString().slice(0, 10);
    input_data.dispatchEvent(new Event('change'));
    console.log(input_data.value);
}
changeTypeDate();

 

calcularValor();

