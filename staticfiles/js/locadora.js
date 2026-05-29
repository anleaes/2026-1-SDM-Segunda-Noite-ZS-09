(function () {
    'use strict';

    function mascaraCpf(valor) {
        valor = valor.replace(/\D/g, '').slice(0, 11);
        if (valor.length > 9) {
            return valor.replace(/(\d{3})(\d{3})(\d{3})(\d{1,2})/, '$1.$2.$3-$4');
        }
        if (valor.length > 6) {
            return valor.replace(/(\d{3})(\d{3})(\d{1,3})/, '$1.$2.$3');
        }
        if (valor.length > 3) {
            return valor.replace(/(\d{3})(\d{1,3})/, '$1.$2');
        }
        return valor;
    }

    function mascaraTelefone(valor) {
        valor = valor.replace(/\D/g, '').slice(0, 11);
        if (valor.length > 10) {
            return valor.replace(/(\d{2})(\d{5})(\d{4})/, '($1) $2-$3');
        }
        if (valor.length > 6) {
            return valor.replace(/(\d{2})(\d{4})(\d{1,4})/, '($1) $2-$3');
        }
        if (valor.length > 2) {
            return valor.replace(/(\d{2})(\d{1,5})/, '($1) $2');
        }
        return valor;
    }

    function mascaraPlaca(valor) {
        return valor.toUpperCase().replace(/[^A-Z0-9]/g, '').slice(0, 7);
    }

    function aplicarMascara(seletor, fn) {
        document.querySelectorAll(seletor).forEach(function (campo) {
            campo.addEventListener('input', function (e) {
                e.target.value = fn(e.target.value);
            });
        });
    }

    function validarSubmit() {
        document.querySelectorAll('form.form-group').forEach(function (form) {
            form.addEventListener('submit', function (e) {
                var acao = form.getAttribute('action') || '';
                if (acao.indexOf('deletar') !== -1) {
                    return;
                }
                var faltando = false;
                form.querySelectorAll('[required]').forEach(function (campo) {
                    if (!(campo.value || '').trim()) {
                        campo.style.borderColor = '#dc2626';
                        campo.style.outline = '2px solid #fecaca';
                        faltando = true;
                    } else {
                        campo.style.borderColor = '';
                        campo.style.outline = '';
                    }
                });

                if (faltando) {
                    alert('Preencha todos os campos obrigatorios.');
                    e.preventDefault();
                    return;
                }

                var cpfs = form.querySelectorAll('input[name="cpf"]');
                for (var i = 0; i < cpfs.length; i++) {
                    var num = cpfs[i].value.replace(/\D/g, '');
                    if (num.length > 0 && num.length !== 11) {
                        alert('CPF invalido. Informe 11 digitos.');
                        cpfs[i].focus();
                        e.preventDefault();
                        return;
                    }
                }
            });
        });
    }

    function hoverLinhas() {
        document.querySelectorAll('table tbody tr').forEach(function (linha) {
            linha.addEventListener('mouseenter', function () {
                linha.style.backgroundColor = '#eff6ff';
            });
            linha.addEventListener('mouseleave', function () {
                linha.style.backgroundColor = '';
            });
        });
    }

    function contarRegistros() {
        var tabela = document.querySelector('table tbody');
        if (!tabela) {
            return;
        }
        var total = 0;
        tabela.querySelectorAll('tr').forEach(function (linha) {
            var td = linha.querySelector('td');
            if (td && td.getAttribute('colspan') === null) {
                total++;
            }
        });
        var titulo = document.querySelector('.container h1');
        if (titulo && total > 0) {
            var span = document.createElement('span');
            span.textContent = ' (' + total + ')';
            span.style.color = '#64748b';
            span.style.fontWeight = '400';
            span.style.fontSize = '0.9em';
            titulo.appendChild(span);
        }
    }

    document.addEventListener('DOMContentLoaded', function () {
        aplicarMascara('input[name="cpf"]', mascaraCpf);
        aplicarMascara('input[name="telefone"]', mascaraTelefone);
        aplicarMascara('input[name="placa"]', mascaraPlaca);
        validarSubmit();
        hoverLinhas();
        contarRegistros();
    });
})();
