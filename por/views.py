import paho.mqtt.client as mqtt
from django.shortcuts import render, redirect
from .models import Team, SensorData
from time import sleep


def team_name(request):
    if request.method == 'POST':
        team_name = request.POST['team_name']
        #team = Team.objects.create(name=team_name)
        team = Team.objects.get_or_create(name=team_name)
        return redirect('data', team_name=team_name)
    return render(request, 'team_name.html')


def data(request, team_name):
    team = Team.objects.get(name=team_name)
    client = mqtt.Client()
    receiving_data = False

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT broker")
        else:
            print("Connection to MQTT broker failed")

    def on_message(client, userdata, msg):
        payload = msg.payload.decode()
        SensorData.objects.create(team=team, data=payload)
        sleep(1)


    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(username="xxjfwlqo:xxjfwlqo", password="9agKXHW-5duIFt7ehaLp6JSM4-L-SMkc")
    client.connect("fly.rmq.cloudamqp.com", 1883, 360)
    client.subscribe("abcd")
    client.loop_start()

    

    if request.method == 'POST':
        if 'start' in request.POST:
            receiving_data = True


        elif 'stop' in request.POST:
            receiving_data = False

    return render(request, 'data.html', {'team': team, 'receiving_data': receiving_data })

def test(request):
    parame = True
    return render(request, 'test.html', {'parame': parame})

