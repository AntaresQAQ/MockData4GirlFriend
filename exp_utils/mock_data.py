def resnet18_ms(x, y):
    if x <= 0:
        return 245
    elif x <=0.01:
        return 83
    elif x <= 0.05:
        return 35
    elif x <= 0.1:
        return 27
    elif x <= 0.5:
        return 10
    else:
        return 5
    
def resnet18_vgg16_gs(x, y):
    if x<=0.01:
        return 0.138 
    elif x<=0.05:
        return 0.120 
    elif x<=0.10:
        return 0.099 
    elif x<=0.50:
        return 0.044 
    else:
        return 0.025 
    
def resnet18_resnet50_gs(x, y):
    if x<=0.01:
        return 0.169
    elif x<=0.05:
        return 0.131
    elif x<=0.10:
        return 0.102
    elif x<=0.50:
        return 0.041
    else:
        return 0.024
    
def resnet18_vgg16_gs2(x, y):
    if x == "mixup": 
        return 0.034
    if x == "cutmix": 
        return 0.036
    if x == "cutout": 
        return 0.103
    if x == "lablesm": 
        return 0.030
    return 0.140

def resnet18_resnet50_gs2(x, y):
    if x == "mixup": 
        return 0.049
    if x == "cutmix": 
        return 0.071
    if x == "cutout": 
        return 0.177
    if x == "lablesm": 
        return 0.023
    return 0.206

mock_funcs = {
    "resnet18-ms": resnet18_ms,
    "resnet18-vgg16-gs": resnet18_vgg16_gs,
    "resnet18-resnet50-gs": resnet18_resnet50_gs,
    "resnet18-vgg16-gs2": resnet18_vgg16_gs2,
    "resnet18-resnet50-gs2": resnet18_resnet50_gs2,
}