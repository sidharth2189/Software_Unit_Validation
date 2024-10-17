/*
 * File: my_model.h
 *
 * Code generated for Simulink model 'my_model'.
 *
 * Model version                  : 1.19
 * Simulink Coder version         : 9.8 (R2022b) 13-May-2022
 * C/C++ source code generated on : Thu Feb 22 15:41:09 2024
 *
 * Target selection: ert.tlc
 * Embedded hardware selection: Intel->x86-64 (Windows64)
 * Code generation objective: Execution efficiency
 * Validation result: Passed (4), Warning (1), Error (0)
 */

#ifndef RTW_HEADER_my_model_h_
#define RTW_HEADER_my_model_h_
#ifndef my_model_COMMON_INCLUDES_
#define my_model_COMMON_INCLUDES_
#include "rtwtypes.h"
#endif                                 /* my_model_COMMON_INCLUDES_ */

#include "my_model_types.h"

/* Macros for accessing real-time model data structure */
#ifndef rtmGetErrorStatus
#define rtmGetErrorStatus(rtm)         ((rtm)->errorStatus)
#endif

#ifndef rtmSetErrorStatus
#define rtmSetErrorStatus(rtm, val)    ((rtm)->errorStatus = (val))
#endif

/* External inputs (root inport signals with default storage) */
typedef struct {
  real_T Inp1;                         /* '<Root>/Inp1' */
} ExtU_my_model_T;

/* External outputs (root outports fed by signals with default storage) */
typedef struct {
  real_T Out1;                         /* '<Root>/Out1' */
} ExtY_my_model_T;

/* Real-time Model Data Structure */
struct tag_RTM_my_model_T {
  const char_T * volatile errorStatus;
};

/* External inputs (root inport signals with default storage) */
extern ExtU_my_model_T my_model_U;

/* External outputs (root outports fed by signals with default storage) */
extern ExtY_my_model_T my_model_Y;

/* Model entry point functions */
extern void my_model_initialize(void);
extern void my_model_step(void);
extern void my_model_terminate(void);

/* Real-time Model object */
extern RT_MODEL_my_model_T *const my_model_M;

/*-
 * The generated code includes comments that allow you to trace directly
 * back to the appropriate location in the model.  The basic format
 * is <system>/block_name, where system is the system number (uniquely
 * assigned by Simulink) and block_name is the name of the block.
 *
 * Use the MATLAB hilite_system command to trace the generated code back
 * to the model.  For example,
 *
 * hilite_system('<S3>')    - opens system 3
 * hilite_system('<S3>/Kp') - opens and selects block Kp which resides in S3
 *
 * Here is the system hierarchy for this model
 *
 * '<Root>' : 'my_model'
 */
#endif                                 /* RTW_HEADER_my_model_h_ */

/*
 * File trailer for generated code.
 *
 * [EOF]
 */
