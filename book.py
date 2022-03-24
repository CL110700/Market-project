def Check_execution(self):
    if not self._buy or not self._sell:
        return False
    if self._buy[0].price>=self._sell[0].price:
        return True
    else:
        return False
