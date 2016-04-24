from nose.tools import assert_raises
from numpy.testing import assert_array_equal, assert_array_almost_equal
import sys
import pandas as pd
from matplotlib import cm, pyplot as plt
import numpy as np
from hmmlearn.hmm import GaussianHMM

# --- read csv by Pandas --- #
feature_name = ['DC X','Time Mean X','Power X','Frequency-domain Entropy X','DC Y','Time Mean Y','Power Y','Frequency-domain Entropy Y','DC Z','Time Mean Z','Power Z','Frequency-domain Entropy Z']
activity_name = ['Activity']

# --- separate feature data and label from each other --- #
# --- both for data csv and test csv --- #
data_df  = pd.read_csv(sys.argv[1])
feature_data = data_df[feature_name]
activity_data = data_df[activity_name]

test_df = pd.read_csv(sys.argv[2])
feature_test = test_df[feature_name]
activity_test = test_df[activity_name]

data_feature = feature_data.as_matrix()
data_label = activity_data.as_matrix()

test_feature = feature_test.as_matrix()
test_label = activity_test.as_matrix()

lengths = data_feature.shape[0]

# --- Run Gaussian HMM --- #
print "fitting to HMM and decoding ..."

# --- Make an HMM instance and execute fit --- #
model = GaussianHMM(n_components=5, covariance_type="diag", n_iter=1000).fit(data_feature)

# --- Predict the optimal sequence of internal hidden state FOR DATA CSV!--- #
# --- the following is generating figure #1, and it predicts state sequence from DATA csv --- #
hidden_states = model.predict(data_feature)

time_axis = np.asarray(range(len(hidden_states)))

# --- fancy plots of different states in HMM --- #
fig1_data,axs = plt.subplots(model.n_components, sharex=True, sharey=True)
fig1_data.suptitle('Estimated State Sequence for Training Data')
colours = cm.rainbow(np.linspace(0, 1, model.n_components))
for i, (ax, colour) in enumerate(zip(axs, colours)):
	# --- Use fancy indexing to plot data in each state --- #
	mask = hidden_states == i
	ax.plot(time_axis[mask], data_feature[:,1][mask], ".", c=colour)
	ax.set_title("{0}th hidden state".format(i))
	ax.grid(True)

# --- the following is generating figure #2, and it plots actual label sequence from DATA csv --- #
fig2_data = plt.figure()
fig2_data.suptitle('Observable Labels from Training Data')
X = np.asarray(time_axis)
Y_temp = np.asarray(data_label[:,0])
Y = np.zeros(len(Y_temp))
for i in range(len(Y_temp)):
	if Y_temp[i] == "downstairs":
		Y[i] = 0
	elif Y_temp[i] == "upstairs":
		Y[i] = 1
	elif Y_temp[i] == "sit":
		Y[i] = 2
	elif Y_temp[i] == "stand":
		Y[i] = 3
	elif Y_temp[i] == "run":
		Y[i] = 4
	else:
		Y[i] = 5

ax2 = fig2_data.add_subplot(111)
ax2.set_xlabel('Time')
ax2.set_ylabel('Activity: 0 - downstairs, 1 - upstairs, 2 - sit, 3 - stand, 4 - run')
plt.plot(X,Y)

# --- Predict the optimal sequence of internal hidden state FOR TEST CSV!--- #
# --- the following is generating figure #3, and it predicts state sequence from test csv --- #
hidden_states = model.predict(test_feature)

time_axis = np.asarray(range(len(hidden_states)))

fig1_test,axs = plt.subplots(model.n_components, sharex=True, sharey=True)
fig1_test.suptitle('Estimated State Sequence for Test Data')
colours = cm.rainbow(np.linspace(0, 1, model.n_components))
for i, (ax, colour) in enumerate(zip(axs, colours)):
	# --- Use fancy indexing to plot data in each state --- #
	mask = hidden_states == i
	ax.plot(time_axis[mask], test_feature[:,1][mask], ".", c=colour)
	ax.set_title("{0}th hidden state".format(i))
	ax.grid(True)

# --- the following is generating figure #2, and it plots actual label sequence from TEST csv --- #
fig2_test = plt.figure()
fig2_test.suptitle('Observable Labels from Test Data')
X = np.asarray(time_axis)
Y_temp = np.asarray(test_label[:,0])
Y = np.zeros(len(Y_temp))
for i in range(len(Y_temp)):
	if Y_temp[i] == "downstairs":
		Y[i] = 0
	elif Y_temp[i] == "upstairs":
		Y[i] = 1
	elif Y_temp[i] == "sit":
		Y[i] = 2
	elif Y_temp[i] == "stand":
		Y[i] = 3
	elif Y_temp[i] == "run":
		Y[i] = 4
	else:
		Y[i] = 5

ax2 = fig2_test.add_subplot(111)
ax2.set_xlabel('Time')
ax2.set_ylabel('Activity: 0 - downstairs, 1 - upstairs, 2 - sit, 3 - stand, 4 - run')
plt.plot(X,Y)


plt.show()
