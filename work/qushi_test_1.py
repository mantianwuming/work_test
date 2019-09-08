import numpy as np

def gradient_descent(X, y, lr=0.01, threshold=1e-6):
    params = np.array([0., 0., 0.])
    ind = 0
    while True:
        p = (X[:,0] * params[0] + X[:,1] * params[1] + params[2])
        # print(p.shape)
        loss = ((p - y) * (p - y)).mean() / 2
        print('loss:', loss)
        if loss < threshold:
            break
        d = (p - y)
        
        # print(d.shape)
        # print(X[:,0].shape)
        # print((d * X[:,0]).mean().shape)
        delta_a = (d * X[:,0]).mean() * lr
        delta_b = (d * X[:,1]).mean() * lr
        delta_c = d.mean() * lr
        # print(delta_a, delta_b, delta_c)
        # break
        delta = np.array([delta_a, delta_b, delta_c])
        params = params - delta 
        print(params)
        # ind += 1
        # if ind == 100:
        #     break
        # print(params)
    return params



if __name__ == '__main__':
    n_samples = 10000
    x_1, x_2 = np.random.random(n_samples), np.random.random(n_samples)
    theta_1, theta_2, b = map(float, input().split())
    # print(theta_1, theta_2, b)
    X, y = np.vstack([x_1, x_2]).T, theta_1 * x_1 + theta_2 * x_2 + b 
    print(X, y)
    print(X.shape)
    # a = np.array([[1,1,1],[2,2,2]])
    # b = np.array([2,2,2])
    # print(a)
    # print(b)
    # print(a*b)
    # c = a[:,0]*b[0] + a[:,1]*b[1] + b[2]
    # print(c)
    # print(c.mean())
    # print(c * c)

    params = gradient_descent(X, y)
    result = []
    print(params)

# if __name__ == "__main__":
#     n_sample = 10000
#     x_1, x_2 = np.random.random(n_sample), np.random.random(n_sample)
#     theta_1, theta_2, b = map(float, input().split())
#     X, y = np.vstack([x_1, x_2]).T, theta_1 * x_1 + theta_2 * x_2 + b
#     params = gradient_descent(X, y)
#     result = []
#     for param in params:
#         result.append('{:.02f}'.format(param))
#     print(' '.join(result))