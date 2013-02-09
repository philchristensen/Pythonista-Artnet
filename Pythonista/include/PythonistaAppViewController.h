//
//  PythonistaAppViewController.h
//
//

#import <UIKit/UIKit.h>

#define kSettingScene32BitColors			@"Scene32BitColors"
#define kSettingSceneAntialiasing			@"SceneAntialiasing"
#define kSettingSceneRetina					@"SceneRetina"

@interface PythonistaAppViewController : UIViewController

- (id)initWithScriptPath:(NSString *)scriptPath backgroundColor:(UIColor *)backgroundColor textColor:(UIColor *)textColor;

@end
