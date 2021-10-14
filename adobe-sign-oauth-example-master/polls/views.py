from django.shortcuts import render
from django.shortcuts import redirect

from django.http import HttpResponse
from django.http import HttpResponseRedirect
import urllib
import requests
import json




def index(request):
    """
    認可コードの取得
    下記に似せて作ってあります
    <?php
    $redirect = 'https://localhost:8443/oauthDemo/callback.php';
    $endpoint = 'https://secure.jp1.echosign.com/public/oauth';

    $params = array(
        'redirect_uri' => $redirect,
        'response_type' => 'code',
        'client_id' => 'CBJCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXhg9-09t',
        'scope' => 'user_login agreement_send'
    );
 
    header("Location: " . $endpoint . '?' . http_build_query($params));
    ?>
    """
    client_id = "*********************"
    redirect = 'https://localhost:8000/oauthDemo/callback'
    endpoint = "https://secure.jp1.adobesign.com/public/oauth/v2"

    params = {
        'redirect_uri' : redirect,
        'response_type' :'code',
        'client_id' : client_id,
        'scope' : 'agreement_read',
    }
    will_redirect = endpoint + "?" + urllib.parse.urlencode(params, quote_via=urllib.parse.quote)
    #return HttpResponse(will_redirect)
    return HttpResponseRedirect(will_redirect)

def callback(request):
    """
    <?php
    $clientId = 'CBJCXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXhg9-09t';      // Sign UI - APIアプリケーション作成時に発行されるID
    $clientSecret = 'QDXXXXXXXXXXXXXXXXXXXXXXXXXXXl6i1';              // Sign UI - APIアプリケーション作成時に発行されるSecret
    $redirect = 'https://localhost:8443/oauthDemo/callback.php';     // Sign UI - APIアプリケーション作成時に指定したRedirect URL

    $data = array(
        'code' => $_GET['code'],                                     // 認可コードの取得で得られる code
        'client_id' => $clientId,
        'client_secret' => $clientSecret,
        'redirect_uri' => $redirect,
        'grant_type' => 'authorization_code'
    );

    $headers = array('Content-Type: application/x-www-form-urlencoded');
    $options = array('http' => array(
        'method' => 'POST',
        'content'=> http_build_query($data),
        'header' => implode("\r\n", $headers)
    ));

    ?>
    """
    client_secret = "*************"
    client_id = "***********"
    redirect = 'https://localhost:8000/oauthDemo/token'
    endpoint = "https://api.jp1.adobesign.com/oauth/v2/token"

    if "code" in request.GET:
        code = request.GET.get("code")
    else:
        return HttpResponse("リクエストに code が含まれていません")

    data = {
        'code' : code,
        'client_id' : client_id,
        'client_secret' : client_secret,
        'redirect_uri' : redirect,
        'grant_type' : 'authorization_code'
    }
    response = requests.post(endpoint, data=data)
    context = json.loads(response.text)
    return render(request, 'polls/index.html', context)
