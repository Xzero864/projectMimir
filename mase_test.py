import pandas as pd


def mase(arr):
    acts = arr[0]
    predictions = arr[1]
    res = {'act':[], 'pred':[], 'err':[]}
    running_total = 1
    index = 0
    last_act = None
    for act, prediction in zip(acts,predictions):
        if not last_act:
            last_act = act
        if not prediction:
            running_total += abs(act - last_act)
            res['act'].append(act)
            res['pred'].append(None)
            res['err'].append(None)
            index += 1
            continue
        err = abs(act - prediction)

        running_total += abs(act - last_act)

        res['act'].append(act)
        res['pred'].append(prediction)
        print(f'{running_total} {index}')
        res['err'].append(err / (running_total / index)) if index != 0 else res['err'].append(err)
        index += 1

    return pd.DataFrame(res)

def preprocess(filename,isframe = False):
    if not isframe:
        frame = pd.read_csv('data/' + filename, index_col=0)
    else:
        frame = filename
    print(frame)
    cleaned_frame = frame.loc[['Actual','Forecast']]
    print(cleaned_frame.loc['Actual'])
    actual, forecast = frame.loc['Actual'], frame.loc['Forecast']
    print(actual[0], forecast[0])
    try:
        actual = (actual.str.rstrip('%').astype('float'))
        forecast = (forecast.str.rstrip('%').astype('float'))
    except Exception as e:
        actual = actual
        forecast = forecast
    return actual,forecast

if __name__ == "__main__":
    import pandas as pd
    actual,forecast = preprocess('data/bfb.csv')
    print(mase([actual,forecast]))




