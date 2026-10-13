## Objetivo

Fazer test_discount_applied_after_coupon passar sem quebrar os testes de tests/test_pricing.py que já passam. A assinatura da funçãoo apply_discount(order, coupon) não pode mudar dado que o checkout depende dela.

## Abordagem

NO arquivo pricing.py o \_percent_off calculava sobre order.subtotal e não sobre o total parcial. Por decisão do usuário, dinheiro é representado em Decimal com ROUND_HALF_UP e quantize(Decimal("0.01")), convertendo o subtotal com Decimal(str(valor)). O projeto exige Python >=3.11.

## Passos concluídos

O pricing.py tem alterações: importa Decimal e ROUND_HALF_UP, tem total = Decimal(str(order.subtotal)) e \_percent_off usa o total parcial com quantize. O teste test_discount_applied_after_coupon passa, e pytest tests/test_pricing.py -q resulta em 1 failed, 6 passed. A assinatura apply_discount(order, coupon) continua inalterada.

## Falha atual

Falha: test_fixed_coupon_never_negative (tests/test_pricing.py:58): subtotal 3.00 com chain(FIXED5) retorna Decimal('-2.00'); esperado Decimal('0.00').
Próximo: \_fixed_off recebe o total parcial e aplica max(Decimal("0"), ...). Depois disso, escrever test_stacked_coupons com dois cupons percentuais em sequência, e rodar pytest sem -x para ver todas as falhas.
