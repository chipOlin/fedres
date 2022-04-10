import urllib3
import requests
from datetime import datetime
from bs4 import BeautifulSoup


urllib3.disable_warnings()


def get_data(url="https://old.bankrot.fedresurs.ru/Messages.aspx"):
    d = datetime.strftime(datetime.now(), '%d.%m.%Y')
    # d = '09.04.2022'
    region = "36"
    # region = ""

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept': '*/*',
    }

    data = 'ctl00%24PrivateOffice1%24ctl00=ctl00%24PrivateOffice1%24ctl00%7Cctl00%24cphBody%24ibMessagesSearch&__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=%2FwEPDwULLTEzMTQ2MTUzNTkPZBYCZg9kFgRmDxQrAAIUKwADDxYCHhdFbmFibGVBamF4U2tpblJlbmRlcmluZ2hkZGRkZAIDD2QWDAIED2QWAgIGDw8WAh8AaGRkAgkPDxYCHgtOYXZpZ2F0ZVVybAUfaHR0cHM6Ly9mZWRyZXN1cnMucnUvbW9uaXRvcmluZ2RkAgsPDxYCHwEFGGh0dHA6Ly93d3cuZmVkcmVzdXJzLnJ1L2RkAhoPZBYCZg8WAh4LXyFJdGVtQ291bnQCAxYGZg9kFgJmDxUDCjA1LjA0LjIwMjI%2BaHR0cHM6Ly9mZWRyZXN1cnMucnUvbmV3cy9jMGM3NjZmZC0zZjA3LTQ1OWMtYTE1ZS1kZjhkNTIzNjA0MTlm0JzQuNGF0LDQudC70L7QstGB0LrQuNC5INCT0J7QmiDQvtGC0LrQsNC30LDQu9GB0Y8g0L7RgiDQvNC%2B0YDQsNGC0L7RgNC40Y8g0L3QsCDQsdCw0L3QutGA0L7RgtGB0YLQstC%2BZAIBD2QWAmYPFQMKMDUuMDQuMjAyMj5odHRwczovL2ZlZHJlc3Vycy5ydS9uZXdzL2ExZmMxNmQ4LWU1MjQtNDBlNS05NGY2LThjNjQ1NTU2OWYwZIsB0J%2FRgNC40L7RgdGC0LDQvdC%2B0LLQutCwINC80L7QvNC10L3RgtCw0LvRjNC90L7QuSDQvtC%2F0LvQsNGC0Ysg0L%2FRg9Cx0LvQuNC60LDRhtC40Lgg0LIg0JXQpNCg0KHQkSA3INCw0L%2FRgNC10LvRjyDRgSAwMjowMCDQtNC%2BIDA1OjAwINC80YHQumQCAg9kFgJmDxUDCjA1LjA0LjIwMjI%2BaHR0cHM6Ly9mZWRyZXN1cnMucnUvbmV3cy85YjY1ZDYyZC0yODJlLTQ0MjgtYTJmZC0zYWFjZTU4NzMyMjWGAtCS0KEg0YDQsNGB0YHQvNC%2B0YLRgNC40YIg0LLQvtC%2F0YDQvtGBINC%2BINCy0L7Qt9C80L7QttC90L7RgdGC0Lgg0YHRg9Cx0L7RgNC00LjQvdCw0YbQuNC4INGC0YDQtdCx0L7QstCw0L3QuNGPINC60YDQtdC00LjRgtC%2B0YDQsCwg0LLRhdC%2B0LTRj9GJ0LXQs9C%2BINCyINC%2B0LTQvdGDINCz0YDRg9C%2F0L%2FRgyDRgSDQtNC%2B0LvQttC90LjQutC%2B0Lwg4oCTINCf0JEgItCe0LvQtdCy0LjQvdGB0LrQuNC5LCDQkdGD0Y7QutGP0L0g0Lgg0L%2FQsNGA0YLQvdC10YDRiyJkAhsPZBYCAgEPFgIfAgIHFg5mD2QWAmYPFQIVaHR0cDovL2thZC5hcmJpdHIucnUvMNCa0LDRgNGC0L7RgtC10LrQsCDQsNGA0LHQuNGC0YDQsNC20L3Ri9GFINC00LXQu2QCAQ9kFgJmDxUCQGh0dHA6Ly93d3cuZWNvbm9teS5nb3YucnUvbWluZWMvYWN0aXZpdHkvc2VjdGlvbnMvQ29ycE1hbmFnbWVudC8v0JzQuNC90Y3QutC%2B0L3QvtC80YDQsNC30LLQuNGC0LjRjyDQoNC%2B0YHRgdC40LhkAgIPZBYCZg8VAhVodHRwOi8vZWdydWwubmFsb2cucnUW0JXQk9Cg0K7QmyDQpNCd0KEg0KDQpGQCAw9kFgJmDxUCJWh0dHA6Ly90ZXN0LmZlZHJlc3Vycy5ydS9kZWZhdWx0LmFzcHgo0KLQtdGB0YLQvtCy0LDRjyDQstC10YDRgdC40Y8g0JXQpNCg0KHQkWQCBA9kFgJmDxUCHmh0dHA6Ly90ZXN0LWZhY3RzLmludGVyZmF4LnJ1LyzQotC10YHRgtC%2B0LLQsNGPINCy0LXRgNGB0LjRjyDQldCk0KDQodCU0K7Qm2QCBQ9kFgJmDxUCJSAgaHR0cDovL2ZvcnVtLWZlZHJlc3Vycy5pbnRlcmZheC5ydS8y0KTQvtGA0YPQvCDQpNC10LTQtdGA0LDQu9GM0L3Ri9GFINGA0LXQtdGB0YLRgNC%2B0LJkAgYPZBYCZg8VAjJodHRwOi8vb2xkLmJhbmtyb3QuZmVkcmVzdXJzLnJ1L0hlbHAvRkFRX0VGUlNCLnBkZjTQp9Cw0YHRgtC%2BINC30LDQtNCw0LLQsNC10LzRi9C1INCy0L7Qv9GA0L7RgdGLIChGQVEpZAIdD2QWBAIBD2QWAmYPZBYCAgEPZBYOAgMPZBYGZg8PZBYCHgdvbmNsaWNrBS5PcGVuTW9kYWxXaW5kb3dfY3RsMDBfY3BoQm9keV9tZHNNZXNzYWdlVHlwZSgpZAIBDw9kFgIfAwUuT3Blbk1vZGFsV2luZG93X2N0bDAwX2NwaEJvZHlfbWRzTWVzc2FnZVR5cGUoKWQCAg8PZBYCHwMFJENsZWFyX2N0bDAwX2NwaEJvZHlfbWRzTWVzc2FnZVR5cGUoKWQCBQ9kFgICAQ9kFgICAQ8QDxYCHgtfIURhdGFCb3VuZGdkEBUbBtCS0YHQtSjQviDQstCy0LXQtNC10L3QuNC4INC90LDQsdC70Y7QtNC10L3QuNGPOdC%2BINCy0LLQtdC00LXQvdC40Lgg0LLQvdC10YjQvdC10LPQviDRg9C%2F0YDQsNCy0LvQtdC90LjRj0PQviDQstCy0LXQtNC10L3QuNC4INGE0LjQvdCw0L3RgdC%2B0LLQvtCz0L4g0L7Qt9C00L7RgNC%2B0LLQu9C10L3QuNGPM9C%2BINC%2F0YDQvtC00LvQtdC90LjQuCDRgdGA0L7QutCwINC%2F0YDQvtGG0LXQtNGD0YDRizPQvtCxINC40LfQvNC10L3QtdC90LjQuCDRgdGD0LTQtdCx0L3QvtCz0L4g0LDQutGC0LAt0L7QsSDQvtGC0LzQtdC90LUg0YHRg9C00LXQsdC90L7Qs9C%2BINCw0LrRgtCwyAHQviDQv9GA0LjQt9C90LDQvdC40Lgg0L7QsdC%2B0YHQvdC%2B0LLQsNC90L3Ri9C8INC30LDRj9Cy0LvQtdC90LjRjyDQviDQv9GA0LjQt9C90LDQvdC40Lgg0LPRgNCw0LbQtNCw0L3QuNC90LAg0LHQsNC90LrRgNC%2B0YLQvtC8INC4INCy0LLQtdC00LXQvdC40Lgg0YDQtdGB0YLRgNGD0LrRgtGD0YDQuNC30LDRhtC40Lgg0LXQs9C%2BINC00L7Qu9Cz0L7Qsn3QviDQv9GA0LjQt9C90LDQvdC40Lgg0LTQvtC70LbQvdC40LrQsCDQsdCw0L3QutGA0L7RgtC%2B0Lwg0Lgg0L7RgtC60YDRi9GC0LjQuCDQutC%2B0L3QutGD0YDRgdC90L7Qs9C%2BINC%2F0YDQvtC40LfQstC%2B0LTRgdGC0LLQsEvQvtCxINC%2B0YLQutCw0LfQtSDQsiDQv9GA0LjQt9C90LDQvdC40Lgg0LTQvtC70LbQvdC40LrQsCDQsdCw0L3QutGA0L7RgtC%2B0LyaAdC%2BINC%2F0YDQuNC80LXQvdC10L3QuNC4INC%2F0YDQuCDQsdCw0L3QutGA0L7RgtGB0YLQstC1INC00L7Qu9C20L3QuNC60LAg0L%2FRgNCw0LLQuNC7INC%2F0LDRgNCw0LPRgNCw0YTQsCDCq9CR0LDQvdC60YDQvtGC0YHRgtCy0L4g0LfQsNGB0YLRgNC%2B0LnRidC40LrQvtCywrtr0L4g0L%2FQtdGA0LXQtNCw0YfQtSDQtNC10LvQsCDQvdCwINGA0LDRgdGB0LzQvtGC0YDQtdC90LjQtSDQtNGA0YPQs9C%2B0LPQviDQsNGA0LHQuNGC0YDQsNC20L3QvtCz0L4g0YHRg9C00LBp0L7QsSDRg9GC0LLQtdGA0LbQtNC10L3QuNC4INC%2F0LvQsNC90LAg0YDQtdGB0YLRgNGD0LrRgtGD0YDQuNC30LDRhtC40Lgg0LTQvtC70LPQvtCyINCz0YDQsNC20LTQsNC90LjQvdCwWtC%2BINC30LDQstC10YDRiNC10L3QuNC4INGA0LXRgdGC0YDRg9C60YLRg9GA0LjQt9Cw0YbQuNC4INC00L7Qu9Cz0L7QsiDQs9GA0LDQttC00LDQvdC40L3QsI4B0L4g0L%2FRgNC40LfQvdCw0L3QuNC4INCz0YDQsNC20LTQsNC90LjQvdCwINCx0LDQvdC60YDQvtGC0L7QvCDQuCDQstCy0LXQtNC10L3QuNC4INGA0LXQsNC70LjQt9Cw0YbQuNC4INC40LzRg9GJ0LXRgdGC0LLQsCDQs9GA0LDQttC00LDQvdC40L3QsKYB0L4g0L3QtdC%2F0YDQuNC80LXQvdC10L3QuNC4INCyINC%2B0YLQvdC%2B0YjQtdC90LjQuCDQs9GA0LDQttC00LDQvdC40L3QsCDQv9GA0LDQstC40LvQsCDQvtCxINC%2B0YHQstC%2B0LHQvtC20LTQtdC90LjQuCDQvtGCINC40YHQv9C%2B0LvQvdC10L3QuNGPINC%2B0LHRj9C30LDRgtC10LvRjNGB0YLQslTQviDQt9Cw0LLQtdGA0YjQtdC90LjQuCDRgNC10LDQu9C40LfQsNGG0LjQuCDQuNC80YPRidC10YHRgtCy0LAg0LPRgNCw0LbQtNCw0L3QuNC90LBH0L4g0LfQsNCy0LXRgNGI0LXQvdC40Lgg0LrQvtC90LrRg9GA0YHQvdC%2B0LPQviDQv9GA0L7QuNC30LLQvtC00YHRgtCy0LBA0L4g0L%2FRgNC10LrRgNCw0YnQtdC90LjQuCDQv9GA0L7QuNC30LLQvtC00YHRgtCy0LAg0L%2FQviDQtNC10LvRg4MB0L4g0LLQvtC30L7QsdC90L7QstC70LXQvdC40Lgg0L%2FRgNC%2B0LjQt9Cy0L7QtNGB0YLQstCwINC%2F0L4g0LTQtdC70YMg0L4g0L3QtdGB0L7RgdGC0L7Rj9GC0LXQu9GM0L3QvtGB0YLQuCAo0LHQsNC90LrRgNC%2B0YLRgdGC0LLQtSlN0L7QsSDRg9GC0LLQtdGA0LbQtNC10L3QuNC4INCw0YDQsdC40YLRgNCw0LbQvdC%2B0LPQviDRg9C%2F0YDQsNCy0LvRj9GO0YnQtdCz0L5t0L7QsSDQvtGB0LLQvtCx0L7QttC00LXQvdC40Lgg0LjQu9C4INC%2B0YLRgdGC0YDQsNC90LXQvdC40Lgg0LDRgNCx0LjRgtGA0LDQttC90L7Qs9C%2BINGD0L%2FRgNCw0LLQu9GP0Y7RidC10LPQvogB0L4g0L%2FRgNC40LfQvdCw0L3QuNC4INC00LXQudGB0YLQstC40LkgKNCx0LXQt9C00LXQudGB0YLQstC40LkpINCw0YDQsdC40YLRgNCw0LbQvdC%2B0LPQviDRg9C%2F0YDQsNCy0LvRj9GO0YnQtdCz0L4g0L3QtdC30LDQutC%2B0L3QvdGL0LzQuNUB0L4g0LLQt9GL0YHQutCw0L3QuNC4INGBINCw0YDQsdC40YLRgNCw0LbQvdC%2B0LPQviDRg9C%2F0YDQsNCy0LvRj9GO0YnQtdCz0L4g0YPQsdGL0YLQutC%2B0LIg0LIg0YHQstGP0LfQuCDRgSDQvdC10LjRgdC%2F0L7Qu9C90LXQvdC40LXQvCDQuNC70Lgg0L3QtdC90LDQtNC70LXQttCw0YnQuNC8INC40YHQv9C%2B0LvQvdC10L3QuNC10Lwg0L7QsdGP0LfQsNC90L3QvtGB0YLQtdC5nQHQvtCxINGD0LTQvtCy0LvQtdGC0LLQvtGA0LXQvdC40Lgg0LfQsNGP0LLQu9C10L3QuNC5INGC0YDQtdGC0YzQuNGFINC70LjRhiDQviDQvdCw0LzQtdGA0LXQvdC40Lgg0L%2FQvtCz0LDRgdC40YLRjCDQvtCx0Y%2FQt9Cw0YLQtdC70YzRgdGC0LLQsCDQtNC%2B0LvQttC90LjQutCwJtCU0YDRg9Cz0LjQtSDRgdGD0LTQtdCx0L3Ri9C1INCw0LrRgtGLJNCU0YDRg9Cz0LjQtcKg0L7Qv9GA0LXQtNC10LvQtdC90LjRjxUbAAIxMQExATkCMjkCMzACMzECMTgBNwIxMAIyNgIyNwIyMAIyMQIxOQIyNAIyNQIyOAE4ATMBNAE2AjIyAjIzAjE3AjEyAjE2FCsDG2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2RkAgcPZBYGZg8PZBYCHwMFLE9wZW5Nb2RhbFdpbmRvd19jdGwwMF9jcGhCb2R5X21kc1B1Ymxpc2hlcigpZAIBDw9kFgIfAwUsT3Blbk1vZGFsV2luZG93X2N0bDAwX2NwaEJvZHlfbWRzUHVibGlzaGVyKClkAgIPD2QWAh8DBSJDbGVhcl9jdGwwMF9jcGhCb2R5X21kc1B1Ymxpc2hlcigpZAILD2QWAmYPEA8WAh8EZ2QQFVgAG9CQ0LvRgtCw0LnRgdC60LjQuSDQutGA0LDQuR%2FQkNC80YPRgNGB0LrQsNGPINC%2B0LHQu9Cw0YHRgtGMKdCQ0YDRhdCw0L3Qs9C10LvRjNGB0LrQsNGPINC%2B0LHQu9Cw0YHRgtGMJ9CQ0YHRgtGA0LDRhdCw0L3RgdC60LDRjyDQvtCx0LvQsNGB0YLRjCfQkdC10LvQs9C%2B0YDQvtC00YHQutCw0Y8g0L7QsdC70LDRgdGC0Ywf0JHRgNGP0L3RgdC60LDRjyDQvtCx0LvQsNGB0YLRjCfQktC70LDQtNC40LzQuNGA0YHQutCw0Y8g0L7QsdC70LDRgdGC0Ywp0JLQvtC70LPQvtCz0YDQsNC00YHQutCw0Y8g0L7QsdC70LDRgdGC0Ywl0JLQvtC70L7Qs9C%2B0LTRgdC60LDRjyDQvtCx0LvQsNGB0YLRjCXQktC%2B0YDQvtC90LXQttGB0LrQsNGPINC%2B0LHQu9Cw0YHRgtGMENCzLiDQnNC%2B0YHQutCy0LAh0LMuINCh0LDQvdC60YIt0J%2FQtdGC0LXRgNCx0YPRgNCzGtCzLiDQodC10LLQsNGB0YLQvtC%2F0L7Qu9GMNtCV0LLRgNC10LnRgdC60LDRjyDQsNCy0YLQvtC90L7QvNC90LDRjyDQvtCx0LvQsNGB0YLRjCPQl9Cw0LHQsNC50LrQsNC70YzRgdC60LjQuSDQutGA0LDQuSPQmNCy0LDQvdC%2B0LLRgdC60LDRjyDQvtCx0LvQsNGB0YLRjEHQmNC90YvQtSDRgtC10YDRgNC40YLQvtGA0LjQuCwg0LLQutC70Y7Rh9Cw0Y8g0LMu0JHQsNC50LrQvtC90YPRgCHQmNGA0LrRg9GC0YHQutCw0Y8g0L7QsdC70LDRgdGC0Yw80JrQsNCx0LDRgNC00LjQvdC%2BLdCR0LDQu9C60LDRgNGB0LrQsNGPINCg0LXRgdC%2F0YPQsdC70LjQutCwLdCa0LDQu9C40L3QuNC90LPRgNCw0LTRgdC60LDRjyDQvtCx0LvQsNGB0YLRjCHQmtCw0LvRg9C20YHQutCw0Y8g0L7QsdC70LDRgdGC0Ywd0JrQsNC80YfQsNGC0YHQutC40Lkg0LrRgNCw0Lk80JrQsNGA0LDRh9Cw0LXQstC%2BLdCn0LXRgNC60LXRgdGB0LrQsNGPINCg0LXRgdC%2F0YPQsdC70LjQutCwJdCa0LXQvNC10YDQvtCy0YHQutCw0Y8g0L7QsdC70LDRgdGC0Ywh0JrQuNGA0L7QstGB0LrQsNGPINC%2B0LHQu9Cw0YHRgtGMJdCa0L7RgdGC0YDQvtC80YHQutCw0Y8g0L7QsdC70LDRgdGC0Ywj0JrRgNCw0YHQvdC%2B0LTQsNGA0YHQutC40Lkg0LrRgNCw0Lkh0JrRgNCw0YHQvdC%2B0Y%2FRgNGB0LrQuNC5INC60YDQsNC5I9Ca0YPRgNCz0LDQvdGB0LrQsNGPINC%2B0LHQu9Cw0YHRgtGMHdCa0YPRgNGB0LrQsNGPINC%2B0LHQu9Cw0YHRgtGMKdCb0LXQvdC40L3Qs9GA0LDQtNGB0LrQsNGPINC%2B0LHQu9Cw0YHRgtGMH9Cb0LjQv9C10YbQutCw0Y8g0L7QsdC70LDRgdGC0Ywl0JzQsNCz0LDQtNCw0L3RgdC60LDRjyDQvtCx0LvQsNGB0YLRjCPQnNC%2B0YHQutC%2B0LLRgdC60LDRjyDQvtCx0LvQsNGB0YLRjCPQnNGD0YDQvNCw0L3RgdC60LDRjyDQvtCx0LvQsNGB0YLRjDDQndC10L3QtdGG0LrQuNC5INCw0LLRgtC%2B0L3QvtC80L3Ri9C5INC%2B0LrRgNGD0LMp0J3QuNC20LXQs9C%2B0YDQvtC00YHQutCw0Y8g0L7QsdC70LDRgdGC0Ywn0J3QvtCy0LPQvtGA0L7QtNGB0LrQsNGPINC%2B0LHQu9Cw0YHRgtGMKdCd0L7QstC%2B0YHQuNCx0LjRgNGB0LrQsNGPINC%2B0LHQu9Cw0YHRgtGMG9Ce0LzRgdC60LDRjyDQvtCx0LvQsNGB0YLRjCfQntGA0LXQvdCx0YPRgNCz0YHQutCw0Y8g0L7QsdC70LDRgdGC0Ywh0J7RgNC70L7QstGB0LrQsNGPINC%2B0LHQu9Cw0YHRgtGMI9Cf0LXQvdC30LXQvdGB0LrQsNGPINC%2B0LHQu9Cw0YHRgtGMGdCf0LXRgNC80YHQutC40Lkg0LrRgNCw0Lkd0J%2FRgNC40LzQvtGA0YHQutC40Lkg0LrRgNCw0Lkh0J%2FRgdC60L7QstGB0LrQsNGPINC%2B0LHQu9Cw0YHRgtGMIdCg0LXRgdC%2F0YPQsdC70LjQutCwINCQ0LTRi9Cz0LXRjx%2FQoNC10YHQv9GD0LHQu9C40LrQsCDQkNC70YLQsNC5LdCg0LXRgdC%2F0YPQsdC70LjQutCwINCR0LDRiNC60L7RgNGC0L7RgdGC0LDQvSPQoNC10YHQv9GD0LHQu9C40LrQsCDQkdGD0YDRj9GC0LjRjyXQoNC10YHQv9GD0LHQu9C40LrQsCDQlNCw0LPQtdGB0YLQsNC9J9Cg0LXRgdC%2F0YPQsdC70LjQutCwINCY0L3Qs9GD0YjQtdGC0LjRjyXQoNC10YHQv9GD0LHQu9C40LrQsCDQmtCw0LvQvNGL0LrQuNGPI9Cg0LXRgdC%2F0YPQsdC70LjQutCwINCa0LDRgNC10LvQuNGPHdCg0LXRgdC%2F0YPQsdC70LjQutCwINCa0L7QvNC4HdCg0LXRgdC%2F0YPQsdC70LjQutCwINCa0YDRi9C8JNCg0LXRgdC%2F0YPQsdC70LjQutCwINCc0LDRgNC40Lkg0K3QuyXQoNC10YHQv9GD0LHQu9C40LrQsCDQnNC%2B0YDQtNC%2B0LLQuNGPLNCg0LXRgdC%2F0YPQsdC70LjQutCwINCh0LDRhdCwICjQr9C60YPRgtC40Y8pQdCg0LXRgdC%2F0YPQsdC70LjQutCwINCh0LXQstC10YDQvdCw0Y8g0J7RgdC10YLQuNGPIC0g0JDQu9Cw0L3QuNGPJ9Cg0LXRgdC%2F0YPQsdC70LjQutCwINCi0LDRgtCw0YDRgdGC0LDQvR3QoNC10YHQv9GD0LHQu9C40LrQsCDQotGL0LLQsCPQoNC10YHQv9GD0LHQu9C40LrQsCDQpdCw0LrQsNGB0LjRjyPQoNC%2B0YHRgtC%2B0LLRgdC60LDRjyDQvtCx0LvQsNGB0YLRjCHQoNGP0LfQsNC90YHQutCw0Y8g0L7QsdC70LDRgdGC0Ywh0KHQsNC80LDRgNGB0LrQsNGPINC%2B0LHQu9Cw0YHRgtGMJdCh0LDRgNCw0YLQvtCy0YHQutCw0Y8g0L7QsdC70LDRgdGC0Ywl0KHQsNGF0LDQu9C40L3RgdC60LDRjyDQvtCx0LvQsNGB0YLRjCfQodCy0LXRgNC00LvQvtCy0YHQutCw0Y8g0L7QsdC70LDRgdGC0Ywj0KHQvNC%2B0LvQtdC90YHQutCw0Y8g0L7QsdC70LDRgdGC0Ywl0KHRgtCw0LLRgNC%2B0L%2FQvtC70YzRgdC60LjQuSDQutGA0LDQuSPQotCw0LzQsdC%2B0LLRgdC60LDRjyDQvtCx0LvQsNGB0YLRjB%2FQotCy0LXRgNGB0LrQsNGPINC%2B0LHQu9Cw0YHRgtGMHdCi0L7QvNGB0LrQsNGPINC%2B0LHQu9Cw0YHRgtGMH9Ci0YPQu9GM0YHQutCw0Y8g0L7QsdC70LDRgdGC0Ywh0KLRjtC80LXQvdGB0LrQsNGPINC%2B0LHQu9Cw0YHRgtGMKdCj0LTQvNGD0YDRgtGB0LrQsNGPINCg0LXRgdC%2F0YPQsdC70LjQutCwJdCj0LvRjNGP0L3QvtCy0YHQutCw0Y8g0L7QsdC70LDRgdGC0Ywf0KXQsNCx0LDRgNC%2B0LLRgdC60LjQuSDQutGA0LDQuUrQpdCw0L3RgtGLLdCc0LDQvdGB0LjQudGB0LrQuNC5INCw0LLRgtC%2B0L3QvtC80L3Ri9C5INC%2B0LrRgNGD0LMgLSDQrtCz0YDQsCXQp9C10LvRj9Cx0LjQvdGB0LrQsNGPINC%2B0LHQu9Cw0YHRgtGMJ9Cn0LXRh9C10L3RgdC60LDRjyDQoNC10YHQv9GD0LHQu9C40LrQsCHQp9C40YLQuNC90YHQutCw0Y8g0L7QsdC70LDRgdGC0Yw40KfRg9Cy0LDRiNGB0LrQsNGPINCg0LXRgdC%2F0YPQsdC70LjQutCwIC0g0KfRg9Cy0LDRiNC40Y8y0KfRg9C60L7RgtGB0LrQuNC5INCw0LLRgtC%2B0L3QvtC80L3Ri9C5INC%2B0LrRgNGD0LM70K%2FQvNCw0LvQvi3QndC10L3QtdGG0LrQuNC5INCw0LLRgtC%2B0L3QvtC80L3Ri9C5INC%2B0LrRgNGD0LMl0K%2FRgNC%2B0YHQu9Cw0LLRgdC60LDRjyDQvtCx0LvQsNGB0YLRjBVYAAExAjEwAjExAjEyAjE0AjE1AjE3AjE4AjE5AjIwAjQ1AjQwAzIwMQI5OQMxMDECMjQDMjAzAjI1AjgzAjI3AjI5AjMwAjkxAjMyAjMzAjM0ATMBNAIzNwIzOAI0MQI0MgI0NAI0NgI0NwMyMDACMjICNDkCNTACNTICNTMCNTQCNTYCNTcBNQI1OAI3OQI4NAI4MAI4MQI4MgIyNgI4NQI4NgI4NwMyMDICODgCODkCOTgDMTAyAjkyAjkzAjk1AjYwAjYxAjM2AjYzAjY0AjY1AjY2ATcCNjgCMjgCNjkCNzACNzECOTQCNzMBOAMxMDMCNzUCOTYCNzYCOTcCNzcDMTA0Ajc4FCsDWGdnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dnZ2dkZAIND2QWBmYPD2QWAh8DBSlPcGVuTW9kYWxXaW5kb3dfY3RsMDBfY3BoQm9keV9tZHNEZWJ0b3IoKWQCAQ8PZBYCHwMFKU9wZW5Nb2RhbFdpbmRvd19jdGwwMF9jcGhCb2R5X21kc0RlYnRvcigpZAICDw9kFgIfAwUfQ2xlYXJfY3RsMDBfY3BoQm9keV9tZHNEZWJ0b3IoKWQCDw9kFggCAw8PZBYEHghvbmNoYW5nZQU2U2V0SGlkZGVuRmllbGRfY3RsMDBfY3BoQm9keV9jbGRyQmVnaW5EYXRlKHRoaXMudmFsdWUpHgpvbmtleXByZXNzBTZTZXRIaWRkZW5GaWVsZF9jdGwwMF9jcGhCb2R5X2NsZHJCZWdpbkRhdGUodGhpcy52YWx1ZSlkAgUPD2QWAh8DBSpTaG93Q2FsZW5kYXJfY3RsMDBfY3BoQm9keV9jbGRyQmVnaW5EYXRlKClkAgYPD2QWBB4FU3R5bGUFMGN1cnNvcjogcG9pbnRlcjsgdmlzaWJpbGl0eTpoaWRkZW47IGRpc3BsYXk6bm9uZR8DBShDbGVhcklucHV0X2N0bDAwX2NwaEJvZHlfY2xkckJlZ2luRGF0ZSgpZAIHDw8WAh4YQ2xpZW50VmFsaWRhdGlvbkZ1bmN0aW9uBSlWYWxpZGF0ZUlucHV0X2N0bDAwX2NwaEJvZHlfY2xkckJlZ2luRGF0ZWRkAhEPZBYIAgMPD2QWBB8FBTRTZXRIaWRkZW5GaWVsZF9jdGwwMF9jcGhCb2R5X2NsZHJFbmREYXRlKHRoaXMudmFsdWUpHwYFNFNldEhpZGRlbkZpZWxkX2N0bDAwX2NwaEJvZHlfY2xkckVuZERhdGUodGhpcy52YWx1ZSlkAgUPD2QWAh8DBShTaG93Q2FsZW5kYXJfY3RsMDBfY3BoQm9keV9jbGRyRW5kRGF0ZSgpZAIGDw9kFgQfBwUwY3Vyc29yOiBwb2ludGVyOyB2aXNpYmlsaXR5OmhpZGRlbjsgZGlzcGxheTpub25lHwMFJkNsZWFySW5wdXRfY3RsMDBfY3BoQm9keV9jbGRyRW5kRGF0ZSgpZAIHDw8WAh8IBSdWYWxpZGF0ZUlucHV0X2N0bDAwX2NwaEJvZHlfY2xkckVuZERhdGVkZAIDD2QWAmYPZBYCAgcPZBYCZg8WAh4Fc3R5bGUFIHBvc2l0aW9uOiByZWxhdGl2ZTsgYm90dG9tOiAyNXB4ZBgCBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WCwUWY3RsMDAkcmFkV2luZG93TWFuYWdlcgUpY3RsMDAkUHJpdmF0ZU9mZmljZTEkaWJQcml2YXRlT2ZmaWNlRW50ZXIFIWN0bDAwJFByaXZhdGVPZmZpY2UxJGNiUmVtZW1iZXJNZQUgY3RsMDAkUHJpdmF0ZU9mZmljZTEkUmFkVG9vbFRpcDEFH2N0bDAwJFByaXZhdGVPZmZpY2UxJGlidFJlc3RvcmUFImN0bDAwJERlYnRvclNlYXJjaDEkaWJEZWJ0b3JTZWFyY2gFFmN0bDAwJGNwaEJvZHkkY2JXaXRoQXUFHWN0bDAwJGNwaEJvZHkkY2JXaXRoVmlvbGF0aW9uBR5jdGwwMCRjcGhCb2R5JGliTWVzc2FnZXNTZWFyY2gFFmN0bDAwJGNwaEJvZHkkaW1nQ2xlYXIFG2N0bDAwJGNwaEJvZHkkaWJFeGNlbEV4cG9ydAUYY3RsMDAkY3BoQm9keSRndk1lc3NhZ2VzDzwrAAwBCAIUZElrWjrjD%2FZVwiaGbPnOu1QtK2Ph&__VIEWSTATEGENERATOR=8EE02EF5&__PREVIOUSPAGE=u0YJjgLPY8IcrrwtjyQQyAByUrDnIF2hgMnHcGz5GQsVuQzVrMYdXP131VSJH6EoLidaUV2RDa6yf_YOiLwgUzYJ6Qk1&ctl00%24PrivateOffice1%24tbLogin=&ctl00%24PrivateOffice1%24tbPassword=&ctl00%24PrivateOffice1%24cbRememberMe=on&ctl00%24PrivateOffice1%24tbEmailForPassword=&ctl00_PrivateOffice1_RadToolTip1_ClientState=&ctl00%24DebtorSearch1%24inputDebtor=%D0%BF%D0%BE%D0%B8%D1%81%D0%BA&ctl00%24cphBody%24tbMessageNumber=&ctl00%24cphBody%24mdsMessageType%24tbSelectedText=%D0%98%D0%BD%D0%BE%D0%B5%20%D1%81%D0%BE%D0%BE%D0%B1%D1%89%D0%B5%D0%BD%D0%B8%D0%B5&ctl00%24cphBody%24mdsMessageType%24hfSelectedValue=Other&ctl00%24cphBody%24mdsMessageType%24hfSelectedType=&ctl00%24cphBody%24ddlCourtDecisionType=&ctl00%24cphBody%24mdsPublisher%24tbSelectedText=&ctl00%24cphBody%24mdsPublisher%24hfSelectedValue=&ctl00%24cphBody%24mdsPublisher%24hfSelectedType=&ctl00%24cphBody%24ucRegion%24ddlBoundList=' + region + '&ctl00%24cphBody%24mdsDebtor%24tbSelectedText=&ctl00%24cphBody%24mdsDebtor%24hfSelectedValue=&ctl00%24cphBody%24mdsDebtor%24hfSelectedType=&ctl00%24cphBody%24cldrBeginDate%24tbSelectedDate=' + d + '&ctl00%24cphBody%24cldrBeginDate%24tbSelectedDateValue=' + d + '&ctl00%24cphBody%24cldrEndDate%24tbSelectedDate=' + d + '&ctl00%24cphBody%24cldrEndDate%24tbSelectedDateValue=' + d + '&__ASYNCPOST=true&ctl00%24cphBody%24ibMessagesSearch.x=41&ctl00%24cphBody%24ibMessagesSearch.y=8'

    response = None

    try:
        response = requests.post(url=url, headers=headers, data=data, verify=False, timeout=0.3)
    except requests.exceptions.ConnectionError as e:
        print(e)
    except requests.exceptions.ReadTimeout as e:
        print(e)

    if response:
        soup = BeautifulSoup(response.content, "lxml")
        table = soup.find("table", id="ctl00_cphBody_gvMessages")
        tr = table.find_all("tr")
        debtor = {}
        if len(tr) > 1:
            tr.pop(0)

            for tr_l in tr:
                dataline = tr_l.find_all("td")
                dt = dataline[0].string.strip()
                link = "https://old.bankrot.fedresurs.ru" + dataline[1].find("a").get("href")
                name_debt = dataline[2].find("a").string.strip()
                if not dt in debtor.keys():
                    debtor[dt] = {"link": link, "name": name_debt}
            return debtor
            # print(debtor)
        else:
            return None
    else:
        return None


def main():
    get_data("https://old.bankrot.fedresurs.ru/Messages.aspx")


if __name__ == '__main__':
    main()
