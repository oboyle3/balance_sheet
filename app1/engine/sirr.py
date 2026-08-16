

    #   product_name 
    #  coupon_rate 
    # funding_cost 
    #credit_loss 
    # servicing_cost 
    # target_margin 
def calculate_sirr(
    coupon_rate, 
    funding_cost,
    credit_loss,
    servicing_cost, 
    target_margin, 
):
    return(
        coupon_rate
        - funding_cost
        - credit_loss
        - servicing_cost
        - target_margin
    )