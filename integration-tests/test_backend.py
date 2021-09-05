import requests
import time

def test_get_backend_version_equals_200():
  response = requests.get("http://backend:5000/")
  assert response.status_code == 200

def test_get_backend_version_name():
  response = requests.get("http://backend:5000/")
  resp_body = response.json()
  assert resp_body["name"] == "Daily Weather Extremes"

def test_get_backend_version_number():
  response = requests.get("http://backend:5000/")
  resp_body = response.json()
  version = resp_body["version"]
  assert version.startswith('v')
  assert "." in version

def test_get_backend_regions_world():
  for t in range(5):
    response = requests.get("http://backend:5000/regions")
    resp_body = response.json()
    if len(resp_body)>0:
      assert resp_body[0][0] == "World"
      return
    else:
      time.sleep(1)
  assert False

def test_get_backend_results_world():
  for t in range(10):
    response = requests.get("http://backend:5000/results/World")
    resp_body = response.json()
    if len(resp_body)>0:
      assert resp_body[0][0] == "World ranking of selected weather parameters"
      return
    else:
      time.sleep(2)
  assert False