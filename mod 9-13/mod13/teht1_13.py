import json
from flask import Flask, request, Response

app = Flask(__name__)
@app.route('/alkuluku/<teksti>')
def alkuluku(teksti):
    try:
        num = int(teksti)
        flag = False
        vast = {
            "number":num
        }
        if num == 0 or num == 1:
            vast["IsPrime"] = False
        elif num > 1:
            # check for factors
            for i in range(2, num):
                if (num % i) == 0:
                    # if factor is found, set flag to True
                    flag = True
                    # break out of loop
                    break

            # check if flag is True
            if flag:
                print(num, "is not a prime number")
                vast["IsPrime"] = False

            else:
                vast["IsPrime"] = True

                print(num, "is a prime number")
        vast_json = json.dumps(vast)
        return Response(vast_json, mimetype='application/json')
    except ValueError:
        tilakoodi = 400
        vastaus = {
            "status": tilakoodi,
            "teksti": "Ei ollut numero"
        }
        vast_json = json.dumps(vastaus)

        return Response(response=vast_json, status=tilakoodi, mimetype='application/json')
if __name__ == '__main__':
    app.run(use_reloader=True, host="127.0.0.1", port=3000)