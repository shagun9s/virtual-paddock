import json

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))

        engine     = body.get('engine', '')
        tyres      = body.get('tyres', '')
        aero       = body.get('aero', '')
        suspension = body.get('suspension', '')
        brakes     = body.get('brakes', '')
        fuel       = body.get('fuel', '')

        es  = {'hybrid-v6-turbo-high':95,'hybrid-v6-turbo-balanced':78,'hybrid-v6-turbo-economy':60}.get(engine, 75)
        ts  = {'soft':90,'medium':72,'hard':58,'intermediate':65,'wet':50}.get(tyres, 70)
        as_ = {'high-downforce':92,'medium-downforce':74,'low-drag':88}.get(aero, 75)
        ss  = {'stiff':85,'medium-s':74,'soft-s':62}.get(suspension, 70)
        bs  = {'carbon-ceramic-race':95,'carbon-ceramic-road':80,'steel':62}.get(brakes, 70)
        fs  = {'low':88,'medium-f':72,'high':52}.get(fuel, 70)

        power           = round(es*0.9  + as_*0.1)
        cornering       = round(as_*0.6 + ts*0.3  + ss*0.1)
        top_speed       = round(es*0.5  + as_*0.3 + fs*0.2)
        braking         = round(bs*0.7  + ts*0.2  + ss*0.1)
        reliability     = round((100-es*0.2)*0.5 + bs*0.2 + fs*0.3)
        balance         = round((ss+as_+ts)/3)
        fuel_efficiency = round(fs*0.7  + es*0.3)
        overall         = round((power+cornering+top_speed+braking+reliability+balance+fuel_efficiency)/7)

        result = {
            "overall": overall,
            "power": power,
            "cornering": cornering,
            "top_speed": top_speed,
            "braking": braking,
            "reliability": reliability,
            "balance": balance,
            "fuel_efficiency": fuel_efficiency,
            "telemetry": {
                "topSpeed": round(280 + (top_speed/100)*70),
                "accel0to100": round(2.9 - (power/100)*1.1, 1),
                "lapDelta": round(((100-overall)/100)*3.5 - 1.5, 2)
            }
        }

        return {
            "statusCode": 200,
            "headers": {
                "Access-Control-Allow-Origin": "*",
                "Content-Type": "application/json"
            },
            "body": json.dumps(result)
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"error": str(e)})
        }
