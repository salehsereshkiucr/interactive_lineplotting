import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons, Slider
import pickle as pickle

# Generate random data for each plot

#TODO: change the root to the location when all the folders are saved.
root = './avg_dics/'

accessions = ['mutation_bias', 'c24', 'ler', 'sha', 'cvi', 'g1001_high05', 'g1001_low05', 'g1001_high1', 'g1001_low01']
tags = {'real', 'prediction', 'context_base'}


tags = {
        'mutation_b_real_all': 'real/avg_dics_mutation_bias_all_real.pkl',
        'mutation_b_real_convs': 'real/avg_dics_mutation_bias_convbase_real.pkl',
        'mutation_b_prediction_all': 'prediction/avg_dics_mutation_bias.pkl',
        'mutation_b_prediction_convs': 'prediction/avg_dics_convbase_mutation_bias_snp_cntx_base_False.pkl',
        'mutation_b_prediction_convs_cntxbase': 'context_base/avg_dics_convbase_mutation_bias_snp_cntx_base-True.pkl',
        'c24_real_all': 'real/avg_dics_c24_all_real.pkl',
        'c24_real_convs': 'real/avg_dics_c24_convbase_real.pkl',
        'c24_prediction_all': 'prediction/avg_dics_c24.pkl',
        'c24_prediction_convs': 'prediction/avg_dics_convbase_c24_snp_cntx_base_False.pkl',
        'c24_prediction_convs_cntxbase': 'context_base/avg_dics_convbase_c24_snp_cntx_base-True.pkl',
        'ler_real_all': 'real/avg_dics_ler_all_real.pkl',
        'ler_real_convs': 'real/avg_dics_ler_convbase_real.pkl',
        'ler_prediction_all': 'prediction/avg_dics_ler.pkl',
        'ler_prediction_convs': 'prediction/avg_dics_convbase_ler_snp_cntx_base_False.pkl',
        'sha_real_all': 'real/avg_dics_sha_all_real.pkl',
        'sha_real_convs': 'real/avg_dics_sha_convbase_real.pkl',
        'sha_prediction_all': 'prediction/avg_dics_sha.pkl',
        'sha_prediction_convs': 'prediction/avg_dics_convbase_sha_snp_cntx_base_False.pkl',
        'cvi_real_all': 'real/avg_dics_cvi_all_real.pkl',
        'cvi_real_convs': 'real/avg_dics_cvi_convbase_real.pkl',
        'cvi_prediction_all': 'prediction/avg_dics_cvi.pkl',
        'cvi_prediction_convs': 'prediction/avg_dics_convbase_cvi_snp_cntx_base_False.pkl',
        'g1001_low05_real_all': 'real/avg_dics_g1001_low05_all_real.pkl',
        'g1001_low05_real_convs': 'real/avg_dics_g1001_low05_convbase_real.pkl',
        'g1001_low05_prediction_all': 'prediction/avg_dics_g1001_low05.pkl',
        'g1001_low05_prediction_convs': 'prediction/avg_dics_convbase_g1001_low05_snp_cntx_base_False.pkl',
        'g1001_high05_real_all': 'real/avg_dics_g1001_high05_all_real.pkl',
        'g1001_high05_real_convs': 'real/avg_dics_g1001_high05_convbase_real.pkl',
        'g1001_high05_prediction_all': 'prediction/avg_dics_g1001_high05.pkl',
        'g1001_high05_prediction_convs': 'prediction/avg_dics_convbase_g1001_high05_snp_cntx_base_False.pkl',
        'g1001_low01_real_all': 'real/avg_dics_g1001_low01_all_real.pkl',
        'g1001_low01_real_convs': 'real/avg_dics_g1001_low01_convbase_real.pkl',
        'g1001_low01_prediction_all': 'prediction/avg_dics_g1001_low01.pkl',
        'g1001_low01_prediction_convs': 'prediction/avg_dics_convbase_g1001_low01_snp_cntx_base_False.pkl',
        'g1001_high1_real_all': 'real/avg_dics_g1001_high1_all_real.pkl',
        'g1001_high1_real_convs': 'real/avg_dics_g1001_high1_convbase_real.pkl',
        'g1001_high1_prediction_all': 'prediction/avg_dics_g1001_high1.pkl',
        'g1001_high1_prediction_convs': 'prediction/avg_dics_convbase_g1001_high1_snp_cntx_base_False.pkl',
        }

tags = {
        'c24_real_all': 'real/avg_dics_c24_all_real.pkl',
        'c24_real_convs': 'real/avg_dics_c24_convbase_real.pkl',
        'c24_prediction_all': 'prediction/avg_dics_c24.pkl',
        'c24_prediction_convs': 'prediction/avg_dics_convbase_c24_snp_cntx_base_False.pkl',
        'c24_prediction_convs_cntxbase': 'context_base/avg_dics_convbase_c24_snp_cntx_base-True.pkl',
        }

plot1_data = []
plot2_data = []
labels = []


def convert_avgs_dic_to_lists(avgs_dic):
    res_1 = []
    res_2 = []
    labels = []
    for key in avgs_dic.keys():
        i = 0
        lst1 =[]
        lst2 = []
        while 'ds-' + str(i) in avgs_dic[key].keys():
            lst1.append(avgs_dic[key]['ds-' + str(i)])
            i+=1
        i = 0
        while 'gbl-' + str(i) in avgs_dic[key].keys():
            lst1.append(avgs_dic[key]['gbl-' + str(i)])
            i+=1
        i = 0
        while 'gbr-' + str(i) in avgs_dic[key].keys():
            lst2.append(avgs_dic[key]['gbr-' + str(i)])
            i+=1
        i = 0
        while 'us-' + str(i) in avgs_dic[key].keys():
            lst2.append(avgs_dic[key]['us-' + str(i)])
            i+=1
        res_1.append(lst1)
        res_2.append(lst2)
        labels.append(key)
    return np.asarray(res_1), np.asarray(res_2), labels

def load_dic(file_name):
    f = open(file_name, "rb")
    res = pickle.load(f)
    f.close()
    print(file_name + ' loaded from a pickle ')
    return res


for tag in tags.keys():
    input_dic = load_dic(root+tags[tag])
    if 'all' in tag:
        input_dic = {'mutation': input_dic}
    res1, res2, ls = convert_avgs_dic_to_lists(input_dic)
    for pl_data in res1:
        plot1_data.append(pl_data)
    for pl_data in res2:
        plot2_data.append(pl_data)
    for lbl in ls:
        labels.append(tag+ str(lbl))

#plot1_data, plot2_data, labels = process.convert_avgs_dic_to_lists(dr.load_dic(root+fn))
labels_indexes = {str(labels[i]): i for i in range(len(labels))}
num_vectors = len(plot1_data)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
visibility = [False] * (num_vectors * 2)
lines1 = [None] * num_vectors
lines2 = [None] * num_vectors
line_labels = [None] * num_vectors
def checkbox_clicked(label):
    index = labels_indexes[str(label)]
    visibility[index] = not visibility[index]
    visibility[index + num_vectors] = not visibility[index + num_vectors]
    lines1[index].set_visible(visibility[index])
    lines2[index].set_visible(visibility[index + num_vectors])
    #line_labels[index].set_visible(visibility[index])
    plt.draw()
ax_check = plt.axes([0.05, 0.1, 0.1, 0.8], frameon=False)
check = CheckButtons(ax_check, labels, visibility)

plt.subplots_adjust(left=0.2)

for i in range(num_vectors):
    vector1 = plot1_data[i]
    vector2 = plot2_data[i]
    lines1[i], = ax1.plot(vector1, visible=False)
    lines2[i], = ax2.plot(vector2, visible=False)
    line_labels[i] = ax1.text(0, np.mean(vector1), f'Line {i+1}')
    line_labels[i].set_visible(False)

check_colors = [line.get_color() for line in lines1]
box_colors = [line.get_color() for line in lines2]

for i, rect in enumerate(check.rectangles):
    rect.set_facecolor(check_colors[i])
    rect.set_edgecolor(check_colors[i])

for label, color in zip(check.labels, check_colors):
    label.set_color(color)

for line, color in zip(check.lines, box_colors):
    line[0].set_color(color)

# Add a slider for y-axis range
ax_slider = plt.axes([0.15, 0.05, 0.7, 0.03])
slider = Slider(ax_slider, 'Y-axis Range', 0, 0.02, valinit=5)

def update_y_axis(val):
    min_val, max_val = ax1.get_ylim()
    ax1.set_ylim(min_val, val)
    ax2.set_ylim(min_val, val)
    plt.draw()

slider.on_changed(update_y_axis)

def toggle_visibility(line, label):
    line.set_visible(not line.get_visible())
    label.set_visible(line.get_visible())
    plt.draw()



check.on_clicked(checkbox_clicked)
plt.show()
