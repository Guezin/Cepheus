import json
from dataclasses import dataclass
from http import HTTPStatus

@dataclass
class Result():
  status_code: HTTPStatus
  obj: dict

  def answer(self) -> object:
    data = {
      "statusCode": self.status_code,
      "headers": {
          "Access-Control-Allow-Origin": "*",
      }
    }

    if self.obj:
      data["body"] = json.dumps(self.obj, ensure_ascii=False).encode('utf8')
      data["headers"]["Content-Type"] = "application/json"

    return data

class Handler():
    def __init__(self, event, context):
      self._event = event
      self._context = context

    @property
    def event(self) -> object:
      return self._event

    def pre_process(self):
      """Realiza o pré processamento das informações."""

    def handler(self) -> Result:
      """Execução do handler do evento."""
      raise NotImplementedError()

    def run(self):
      try:
        self.pre_process()

        res = self.handler()

        if not isinstance(res, Result):
            raise TypeError("handler result is not a Result")

        return res.answer()

      except Exception as err:
          print(f'exception received: {err}')