class Responses:
    @staticmethod
    def success(result, message: str = "success") -> dict:
        return {
            "status": "success",
            "message": message,
            "result": result,
        }

    @staticmethod
    def error(message: str = "error") -> dict:
        return {
            "status": "error",
            "message": message,
            "result": None,
        }
